import requests
from config import NEWSAPI_KEY, NEWS_SOURCES
from datetime import datetime, timedelta

def fetch_financial_news():
    """Fetch financial news from multiple sources"""
    
    all_articles = []
    
    # Get news from yesterday (so we have fresh content each morning)
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    for source in NEWS_SOURCES:
        print(f"Fetching news from {source}...")
        
        # NewsAPI endpoint
        url = "https://newsapi.org/v2/everything"
        
        params = {
            'sources': source,
            'from': yesterday,
            'sortBy': 'publishedAt',
            'apiKey': NEWSAPI_KEY,
            'pageSize': 5  # Get top 5 articles per source
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Check for errors
            
            data = response.json()
            articles = data.get('articles', [])
            all_articles.extend(articles)
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching from {source}: {e}")
    
    return all_articles

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
