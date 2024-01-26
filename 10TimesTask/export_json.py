# view_db.py
import json
from app import create_app, db, NewsArticle

def export_to_json():
    app = create_app()
    app.app_context().push()

    # Query the NewsArticle table
    articles = NewsArticle.query.all()

    # Specify the JSON file path
    json_file_path = 'news_articles.json'

    # Convert data to a list of dictionaries
    data = [
        {'Title': article.title, 'Category': article.category, 'Publication Date': str(article.publication_date), 'Source URL': article.source_url}
        for article in articles
    ]

    # Write data to the JSON file
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=2)

    print(f'Data exported to {json_file_path}')

if __name__ == '__main__':
    export_to_json()
