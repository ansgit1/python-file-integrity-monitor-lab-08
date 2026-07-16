import hashlib
import json
import smtplib
import time
from email.message import EmailMessage
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import EMAIL_ADDRESS, APP_PASSWORD, RECIPIENTS

file_path = Path("test_files/sample.txt").resolve()


def get_hash():
    with open(file_path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


def send_email():
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

            for recipient in RECIPIENTS:
                msg = EmailMessage()
                msg["Subject"] = "File Integrity Alert"
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = recipient

                msg.set_content(f"""
ALERT!

Dear Recipient,

The monitored file has been modified.

File: {file_path.name}
Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Please verify whether this change was authorized.
""")

                smtp.send_message(msg)
                print(f"Email sent to {recipient}")

    except Exception as e:
        print("Email failed:", e)


def check_integrity():
    current_hash = get_hash()

    with open("baseline.json", "r") as file:
        baseline = json.load(file)

    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if current_hash == baseline["sha256"]:
        print("Integrity OK")
    else:
        print("ALERT! File has been modified.")

        with open("integrity.log", "a") as log:
            log.write(
                f"{log_time} - ALERT - {file_path.name} has been modified\n"
            )

        send_email()


class IntegrityMonitor(FileSystemEventHandler):
    def on_modified(self, event):
        if Path(event.src_path).resolve() == file_path:
            check_integrity()


print("Monitoring started... Press Ctrl+C to stop.")
check_integrity()

observer = Observer()
observer.schedule(
    IntegrityMonitor(),
    path=str(file_path.parent),
    recursive=False
)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()