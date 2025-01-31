import os

from app import app

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.secret_key = os.getenv('SECRET_KEY')
    app.run(debug=True)