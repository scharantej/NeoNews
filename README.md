## Overview
To build a Flask application that showcases recent news articles, we'll employ its robust routing system and HTML templating capabilities. Let's dive into the details:

## HTML Files
**1. index.html**
   - This will serve as the homepage, presenting a list of news articles.
   - It should include elements like `<ul>`, `<li>`, and `<a>` to structure the news article list.

## Routes
**1. @app.route('/')**
   - This route will handle requests to the homepage, where we'll display the index.html.
   - The view function will query a news API to fetch recent articles and pass them to the template.

**2. @app.route('/article/<int:article_id>')**
   - This route will handle requests to individual news articles, presenting their detailed content.
   - The view function will retrieve the article's details from the API based on the provided article ID.

## Implementation
The Python Flask code for these routes and HTML files will look something like this:

```python
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
```

By implementing this design, you can create a fully functional Flask application that showcases recent news articles, allowing users to browse and view individual article details.