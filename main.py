
# Importing necessary modules
from flask import Flask, render_template, request
import requests

# Creating a Flask app instance
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def index():
    # Fetch recent news articles from an API
    articles = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY').json()['articles']
    # Render the homepage with the retrieved articles
    return render_template('index.html', articles=articles)

# Define the article details route
@app.route('/article/<int:article_id>')
def article(article_id):
    # Fetch the specific article details from an API
    article = requests.get('https://newsapi.org/v2/articles?id={}&apiKey=YOUR_API_KEY'.format(article_id)).json()['articles'][0]
    # Render the article details page with the retrieved article
    return render_template('article.html', article=article)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
