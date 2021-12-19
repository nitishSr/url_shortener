import app
from app import db

class UrlShortener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False, unique=True)
    shortened_url = db.Column(db.String(240), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"UrlShortener('{self.original_url}', '{self.shortened_url}')"