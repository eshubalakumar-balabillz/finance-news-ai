import requests
from config import NEWSAPI_KEY

def fetch_financial_news():
    """Fetch financial news from premium sources only"""
    
    all_articles = []
    
    # Premium financial news sources
    sources = [
        'financial-times',
        'bloomberg',
        'reuters',
        'cnbc',
        'the-wall-street-journal',
        'bbc-news',
        'the-economist',
        'ft.com'
    ]
    
    url = "https://newsapi.org/v2/everything"
    
    for source in sources:
        print(f"Fetching news from '{source}'...")
        
        params = {
            'sources': source,
            'sortBy': 'publishedAt',
            'apiKey': NEWSAPI_KEY,
            'pageSize': 5,
            'language': 'en'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            articles = data.get('articles', [])
            all_articles.extend(articles)
            print(f"✅ Found {len(articles)} articles from '{source}'")
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching '{source}': {e}")
    
    # Remove duplicates
    seen_urls = set()
    unique_articles = []
    for article in all_articles:
        if article['url'] not in seen_urls:
            seen_urls.add(article['url'])
            unique_articles.append(article)
    
    return unique_articles
