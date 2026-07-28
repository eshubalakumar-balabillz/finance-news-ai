import os
import schedule
import time
from datetime import datetime
from fetch_news import fetch_finance_news
from send_email import send_email
from dotenv import load_dotenv

load_dotenv()

def job():
    print(f"[{datetime.now()}] Running scheduled task...")
    try:
        news = fetch_finance_news()
        recipient_email = os.getenv("RECIPIENT_EMAIL")
        send_email(recipient_email, news)
        print(f"[{datetime.now()}] Email sent successfully!")
    except Exception as e:
        print(f"[{datetime.now()}] Error: {e}")

# Schedule the job for 7:00 AM every day
schedule.every().day.at("07:00").do(job)

print("Scheduler started. Waiting for 7:00 AM...")

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(60)
