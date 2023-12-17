from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the article summaries into a DataFrame
articles = pd.read_csv('headline.csv')

@app.route('/')
def home():
    # Convert the DataFrame to a list of dicts for easier processing in the template
    articles_list = articles.to_dict('records')
    # Render the home.html template and pass the articles to it
    return render_template('home.html', articles=articles_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)