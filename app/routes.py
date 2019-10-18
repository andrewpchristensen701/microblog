from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'You'}
    posts = [
        {
            'author': {'username': 'Him'},
            'body': 'AHHHHHHHHHHHHHH'
        },
        {
            'author': {'username': 'Her'},
            'body': 'Help me'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)