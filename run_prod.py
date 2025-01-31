import os

from app import app

app.secret_key = os.environ.get('SECRET_KEY')
app.config['ENV'] = 'production'

