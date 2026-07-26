from flask import Flask, render_template
from fetch_news import fetch_financial_news
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Display the news homepage"""
    print("Fetching news...")
    articles = fetch_financial_news()
    
    # Group articles by source
    articles_by_source = {}
    for article in articles:
        source = article['source']['name']
        if source not in articles_by_source:
            articles_by_source[source] = []
        articles_by_source[source].append(article)
    
    current_date = datetime.now().strftime('%B %d, %Y')
    
    return render_template('index.html', 
                         articles_by_source=articles_by_source,
                         current_date=current_date)

if __name__ == '__main__':
    print("Starting Finance News App...")
    app.run(debug=True, port=5000)
