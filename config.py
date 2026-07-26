import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# NewsAPI Configuration
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

# Email Configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Financial news sources
NEWS_SOURCES = [
    "financial-times",
    "bloomberg",
    "reuters",
    "cnbc",
    "the-wall-street-journal"
]

# Schedule time (24-hour format) - 7 AM
SCHEDULE_TIME = "07:00"
