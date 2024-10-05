
import requests
from textblob import TextBlob

def fetch_news(api_key, query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    news_data = response.json()
    return news_data['articles']

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def get_sentiment_score(news_articles):
    sentiment_score = 0
    for article in news_articles:
        sentiment_score += analyze_sentiment(article['title'] + ' ' + article['description'])
    return sentiment_score / len(news_articles)

if __name__ == "__main__":
    api_key = 'your_news_api_key'
    query = 'Indian stock market'
    news_articles = fetch_news(api_key, query)
    sentiment_score = get_sentiment_score(news_articles)
    print(f"Sentiment Score: {sentiment_score}")
