import schedule
import time
from send_email import send_daily_email
from config import SCHEDULE_TIME
from datetime import datetime

def job():
    """Job to run at scheduled time"""
    print(f"\n{'='*60}")
    print(f"[{datetime.now()}] Running scheduled news email job...")
    print(f"{'='*60}")
    send_daily_email()

# Schedule the job
schedule.every().day.at(SCHEDULE_TIME).do(job)

print(f"✅ Scheduler started!")
print(f"📧 News will be sent daily at {SCHEDULE_TIME}")
print(f"To stop, press Ctrl + C")

# Keep scheduler running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute if a job needs to run
