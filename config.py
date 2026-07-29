import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')

# Schedule time (24-hour format) - 6:30 AM EST (10:30 UTC)
SCHEDULE_TIME = "10:30"

