#!/usr/bin/env python3

import time
import psutil
from mailjet_rest import Client

# ------------------------
# ✉️ Mailjet Credentials
# ------------------------
api_key = "0c2ae242ea2bb185f7371fc46a0336b7"
api_secret = "0cee12175cdd0401b0740adc9b31da25"

# ------------------------
# 🕒 Get Current Time
# ------------------------
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

# ------------------------
# ⚠️ Thresholds
# ------------------------
CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50

# ------------------------
# 📧 Function to Send Alert
# ------------------------
def send_alert(subject, message):
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "muhirwa232@gmail.com",
                    "Name": "24/7 SysMon"
                },
                "To": [
                    {
                        "Email": "itsjd232@gmail.com",
                        "Name": "Admin"
                    }
                ],
                "Subject": subject,
                "HTMLPart": f"<h3>{message}</h3>"
            }
        ]
    }
    try:
        result = mailjet.send.create(data=data)
        print(f"✅ Email sent: {result.status_code}")
    except Exception as e:
        print(f"❌ Failed to send email: {str(e)}")

# ------------------------
# 📊 Collect System Metrics
# ------------------------
cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

# ------------------------
# 📥 Create Alert Message
# ------------------------
alert_message = ""

if cpu_usage > CPU_THRESHOLD:
    alert_message += f"⚠️ CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"

if ram_usage > RAM_THRESHOLD:
    alert_message += f"⚠️ RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"

if disk_usage > DISK_THRESHOLD:
    alert_message += f"⚠️ Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}% free)\n"

# ------------------------
# 🚨 Send Alert or Print Normal Status
# ------------------------
if alert_message:
    send_alert(f"🚨 System Alert - {formatted_time}", alert_message)
else:
    print("✅ All system metrics are within normal limits.")
