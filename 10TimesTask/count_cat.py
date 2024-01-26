# view_db.py
from app import create_app, db, NewsArticle

def count_feeds_by_category():
    app = create_app()
    app.app_context().push()

    # Query the NewsArticle table and count feeds for each category
    categories = ['Terrorism/Protest/Political Unrest/Riot', 'Positive/Uplifting', 'Natural Disasters', 'Others']

    for category in categories:
        count = NewsArticle.query.filter_by(category=category).count()
        print(f"Category: {category}, Total Feeds: {count}")

if __name__ == '__main__':
    count_feeds_by_category()
