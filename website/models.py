from . import db

class Tweet(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(20))
    data = db.Column(db.String(150))
    