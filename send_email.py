import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fetch_news import fetch_financial_news
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT_EMAIL
from datetime import datetime

def create_email_html(articles):
    """Create HTML email content with articles"""
    
    current_date = datetime.now().strftime('%B %d, %Y')
    
    # Group articles by source
    articles_by_source = {}
    for article in articles:
        source = article['source']['name']
        if source not in articles_by_source:
            articles_by_source[source] = []
        articles_by_source[source].append(article)
    
    # Start HTML
    html = f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f5f5f5; }}
                .container {{ max-width: 700px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; }}
                header {{ text-align: center; color: #667eea; margin-bottom: 30px; border-bottom: 2px solid #667eea; padding-bottom: 15px; }}
                h1 {{ margin: 0; font-size: 28px; }}
                .date {{ color: #666; font-size: 14px; margin-top: 5px; }}
                .source-section {{ margin-bottom: 25px; }}
                .source-title {{ background-color: #667eea; color: white; padding: 10px 15px; border-radius: 5px; font-weight: bold; margin-bottom: 15px; }}
                .article {{ margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px solid #eee; }}
                .article:last-child {{ border-bottom: none; }}
                .article-title {{ font-size: 16px; font-weight: bold; margin-bottom: 5px; }}
                .article-title a {{ color: #667eea; text-decoration: none; }}
                .article-meta {{ color: #999; font-size: 12px; margin-bottom: 8px; }}
                .article-description {{ color: #555; font-size: 14px; line-height: 1.6; margin-bottom: 8px; }}
                .read-more {{ color: #667eea; text-decoration: none; font-weight: bold; }}
                .footer {{ text-align: center; margin-top: 30px; padding-top: 15px; border-top: 1px solid #eee; color: #999; font-size: 12px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <header>
                    <h1>📊 Daily Finance News</h1>
                    <div class="date">{current_date}</div>
                </header>
    """
    
    # Add articles grouped by source
    for source, source_articles in articles_by_source.items():
        html += f'<div class="source-section"><div class="source-title">{source}</div>'
        
        for article in source_articles:
            html += f"""
                <div class="article">
                    <div class="article-title">
                        <a href="{article['url']}">{article['title']}</a>
                    </div>
                    <div class="article-meta">Published: {article['publishedAt'][:10]}</div>
            """
            
            if article.get('description'):
                html += f'<div class="article-description">{article["description"]}</div>'
            
            html += f'<a href="{article["url"]}" class="read-more">Read Full Article →</a></div>'
        
        html += '</div>'
    
    # Close HTML
    html += """
                <div class="footer">
                    <p>This is your automated daily finance news digest. Stay informed about the markets!</p>
                </div>
            </div>
        </body>
    </html>
    """
    
    return html

def send_daily_email():
    """Fetch news and send email"""
    
    try:
        print(f"[{datetime.now()}] Fetching financial news...")
        articles = fetch_financial_news()
        
        if not articles:
            print("No articles found, skipping email.")
            return False
        
        print(f"[{datetime.now()}] Creating email with {len(articles)} articles...")
        email_html = create_email_html(articles)
        
        # Create email
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Daily Finance News - {datetime.now().strftime('%B %d, %Y')}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        
        # Attach HTML
        msg.attach(MIMEText(email_html, 'html'))
        
        # Send email
        print(f"[{datetime.now()}] Sending email to {RECIPIENT_EMAIL}...")
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        print(f"[{datetime.now()}] ✅ Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"[{datetime.now()}] ❌ Error sending email: {e}")
        return False

if __name__ == "__main__":
    send_daily_email()
