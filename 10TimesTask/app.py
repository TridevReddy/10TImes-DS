# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)

class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    category = db.Column(db.String(50))
    publication_date = db.Column(db.DateTime)
    source_url = db.Column(db.String(255), unique=True)

def create_app():
    return app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
