import requests
from config import NEWSAPI_KEY
from datetime import datetime

# Test the API directly
url = "https://newsapi.org/v2/everything"

params = {
    'q': 'stocks',
    'sortBy': 'publishedAt',
    'apiKey': NEWSAPI_KEY,
    'pageSize': 5,
    'language': 'en'
}

print("Testing NewsAPI...")
print(f"API Key: {NEWSAPI_KEY[:10]}...")
print(f"URL: {url}")
print(f"Params: {params}")
print()

response = requests.get(url, params=params)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
