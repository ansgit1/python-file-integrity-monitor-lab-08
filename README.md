# ## About This Project

This project demonstrates a practical implementation of file integrity monitoring using Python. It monitors a file in real time, detects unauthorized changes using SHA-256 hashing, records security events in a log file, and sends email alerts to one or more recipients.

I created this project as part of my cybersecurity portfolio to demonstrate practical knowledge of file integrity monitoring, security automation, event logging, and email alerting using Python.


---

# Features

* Real-time file monitoring
* SHA-256 file integrity verification
* Email alerts to multiple recipients
* Event logging
* Automatic startup using Windows Task Scheduler (optional)
* Simple and lightweight Python application

---

# Project Workflow

```text
File Modified
      │
      ▼
Watchdog detects the change
      │
      ▼
SHA-256 hash is calculated
      │
      ▼
Compared with the baseline hash
      │
      ▼
Integrity log is updated
      │
      ▼
Email alert is sent to all recipients
```

---

# Lab Environment

## Host Machine

* Windows 11

## Virtual Machine

* VMware Workstation
* Windows 10 Virtual Machine

## Network

* VMware network adapter configured to provide Internet access for Gmail SMTP email notifications.

## Software

| Software                     | Purpose                                                 |
| ---------------------------- | ------------------------------------------------------- |
| Python 3.13                  | Runs the File Integrity Monitor.                        |
| Notepad (or any text editor) | Used to edit the Python scripts.                        |
| Windows Task Scheduler       | Automatically starts the monitor when the user logs on. |

---

# Dependencies

## External Python Package

The following package must be installed before running the project.

| Package        | Purpose                                                                                                                                               |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| watchdog 6.0.0 | A third-party Python package installed from the Python Package Index (PyPI). It monitors the file system in real time and detects file modifications. |

Install it using:

```bash
pip install -r requirements.txt
```

---

## Built-in Python Libraries

These libraries are included with Python and do not require installation.

| Library       | Purpose                                              |
| ------------- | ---------------------------------------------------- |
| hashlib       | Generates SHA-256 hashes to verify file integrity.   |
| json          | Reads the stored baseline hash from `baseline.json`. |
| smtplib       | Sends email alerts using Gmail SMTP.                 |
| email.message | Creates and formats email messages.                  |
| pathlib       | Handles file and folder paths.                       |
| datetime      | Adds timestamps to logs and email alerts.            |
| time          | Keeps the monitoring process running continuously.   |

---

# Project Structure

```text
FileIntegrityMonitor/
│── README.md
│── monitor.py
│── config_example.py
│── requirements.txt
│── baseline.json
│── integrity.log
│── test_files/
│    └── sample.txt
│── screenshots/
│    ├── project_files.png
│    ├── email_configuration.png
│    ├── real_time_monitoring.png
│    └── email_alert.png
```

---

# Installation

1. Install Python 3.13 or later.
2. Install the required package.

```bash
pip install -r requirements.txt
```

---

# Configuration

Rename `config_example.py` to `config.py`.

Update the following information:

* Your Gmail address
* Your Gmail App Password
* Recipient email addresses

Example:

```python
EMAIL_ADDRESS = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"

RECIPIENTS = [
    "recipient1@example.com",
    "recipient2@example.com"
]
```

---

# Running the Project

Open Command Prompt inside the project folder and run:

```bash
py monitor.py
```

The application will continue monitoring the selected file until it is stopped.

---

# Optional: Run Automatically at Windows Logon

Windows Task Scheduler can automatically start the monitor every time the user logs on.

**Program/script**

```text
C:\Users\Administrator.PC2\AppData\Local\Programs\Python\Python313\python.exe
```

**Arguments**

```text
monitor.py
```

**Start in**

```text
C:\Users\Administrator.PC2\Desktop\FileIntegrityMonitor
```

---

# Screenshots

### Project Files

`project_files.png`

### Email Configuration

`email_configuration.png`

### Real-Time Monitoring

`real_time_monitoring.png`

### Email Alert

`email_alert.png`

---

# What I Learned

* Creating a File Integrity Monitor using Python.
* Using SHA-256 hashing to detect file modifications.
* Monitoring files in real time using Watchdog.
* Sending email alerts using Gmail SMTP.
* Logging security events.
* Automating the application with Windows Task Scheduler.
* Organizing a cybersecurity project for GitHub.
