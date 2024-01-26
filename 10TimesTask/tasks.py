# tasks.py
from celery_config import celery
from app import db, NewsArticle, create_app
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from datetime import datetime
from dateutil import parser as date_parser
import feedparser

app = create_app()
app.app_context().push()

stop_words = set(stopwords.words('english'))

@celery.task
def process_rss_feed(feed_url):
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        title = entry.title
        #content = entry.summary
        content = getattr(entry, 'summary', '')
        #publication_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
        try:
            publication_date = date_parser.parse(entry.published)
        except ValueError:
            publication_date = None
        source_url = entry.link

        if publication_date:
            category = classify_category(content)
            article = NewsArticle(title=title, content=content, category=category,
                                  publication_date=publication_date, source_url=source_url)
            db.session.add(article)
            db.session.commit()

        if not NewsArticle.query.filter_by(source_url=source_url).first():
            category = classify_category(content)
            article = NewsArticle(title=title, content=content, category=category,
                                  publication_date=publication_date, source_url=source_url)
            db.session.add(article)
            db.session.commit()

def classify_category(content):
    words = set(word_tokenize(content.lower()))

    terrorism_keywords = {'terrorism', 'terror', 'war', 'boycott', 'bomb', 'bombing', 'violence', 'protest', 'political', 'unrest', 'riot'}
    positive_keywords = {'positive', 'uplifting', 'saved', 'freed', 'survived'}
    natural_disasters_keywords = {'natural', 'floods', 'flooding','accident', 'earthquake', 'tsunami', 'disasters'}

    for keyword_list, category in zip(
            [terrorism_keywords, positive_keywords, natural_disasters_keywords],
            ['Terrorism/Protest/Political Unrest/Riot', 'Positive/Uplifting', 'Natural Disasters']
    ):
        if any(keyword in words for keyword in keyword_list):
            return category

    return 'Others'
