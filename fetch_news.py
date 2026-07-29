import requests
from config import NEWSAPI_KEY
from datetime import datetime, timedelta

def fetch_financial_news():
    """Fetch financial news using keywords"""
    
    all_articles = []
    
    # Use keywords instead of sources
    keywords = ['finance', 'stocks', 'market', 'economy', 'business']
    
    for keyword in keywords:
        print(f"Fetching news for '{keyword}'...")
        
        url = "https://newsapi.org/v2/everything"
        
        params = {
            'q': keyword,
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
            print(f"✅ Found {len(articles)} articles for '{keyword}'")
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching '{keyword}': {e}")
    
    # Remove duplicates
    seen_urls = set()
    unique_articles = []
    for article in all_articles:
        if article['url'] not in seen_urls:
            seen_urls.add(article['url'])
            unique_articles.append(article)
    
    return unique_articles

def display_articles(articles):
    """Display articles in a nice format"""
    
    print("\n" + "="*80)
    print(f"FINANCIAL NEWS DIGEST - {datetime.now().strftime('%B %d, %Y')}")
    print("="*80 + "\n")
    
    if not articles:
        print("No articles found.")
        return
    
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Published: {article['publishedAt'][:10]}")
        print(f"   URL: {article['url']}")
        print()

if __name__ == "__main__":
    print("Fetching latest financial news...")
    articles = fetch_financial_news()
    display_articles(articles)
