from flask import Flask, render_template, request
from automate import summarize_article, analyse_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ''
    sentiment = ''
    if request.method == 'POST':
        url = request.form.get('url')
        summary = summarize_article(url)
        sentiment = analyse_sentiment(summary)
    return render_template('home.html', summary=summary, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)