# view_db.py
from app import create_app, db, NewsArticle

def view_database():
    app = create_app()
    app.app_context().push()

    # Query the NewsArticle table and print the results
    articles = NewsArticle.query.all()

    for article in articles:
        print(f"Title: {article.title}")
        print(f"Category: {article.category}")
        print(f"Publication Date: {article.publication_date}")
        print(f"Source URL: {article.source_url}")
        print("-----")

if __name__ == '__main__':
    view_database()
