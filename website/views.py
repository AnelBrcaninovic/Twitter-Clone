from flask import Blueprint, render_template, request, flash
from . import db
from .models import Tweet


views =Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'] )
def homepage():
    if request.method == 'POST':
        name = request.form.get('name')
        data = request.form.get('data')

        if len(name) > 20:
            flash( 'Name too long' ,category='error')
        elif len(name)< 2:
            flash( 'Name too short' ,category='error')
        elif len(data) > 150:
            flash( 'Write less' ,category='error')
        elif len(data)<2:
            flash( 'Write more' ,category='error')

        else:
            flash('Tweet Sent', category='success')
            new_tweet = Tweet(username = name, data=data)
            db.session.add(new_tweet)
            db.session.commit()


    all_tweets = Tweet.query.all()

    n=Tweet.query.count()

    tweets=[]
    for i in range(n-4, n+1):
        tweets.append(Tweet.query.get(i))
    
    tweets = tweets[::-1]

    return render_template('homepage.html', tweets = tweets )