import pandas as pd
import numpy as np
from GoogleNews import GoogleNews
from utils.helper import newsfeed
from utils.arg_parse import parse_arguments
from models.sentiment_analysis_model import create_sentiment_analysis_model
from models.text_summarization_model import create_text_summarization_model
from web_scraper import WebScraper

scraper = WebScraper()
sentiment_model = create_sentiment_analysis_model()
summarization_model = create_text_summarization_model()


def summarize_article(url):
    scraper = WebScraper()
    # summarizer = TextSummarizationModel()
    article_text = scraper.scrape(url)
    return summarization_model.summarize(article_text)


def analyse_sentiment(title):
    return sentiment_model.apply_model(title)


def main():
    args = parse_arguments()
    google_news = GoogleNews(lang='en', region='UK')
    google_news.set_time_range(args.lower_date, args.upper_date)

    key_words = list(args.key_words)

    article_info = pd.DataFrame(
        columns=['Date', 'Time', 'Title', 'Articles', 'Link'])

    # Dataframe containing the news of all the keywords searched
    articles = pd.DataFrame()

    # Each keyword will be searched separately and results will be saved in a dataframe
    for steps in range(len(key_words)):
        string = (key_words[steps])
        google_news.search(string)

        # Fetch the results
        result = google_news.results()

        for steps in range(args.n_pages):
            # Variable consists of pages specified by user so using "for loop" to retrieve all the data in dataframe
            google_news.get_page(steps)
            feed = newsfeed(article_info, result)

            articles = pd.concat([articles, feed], ignore_index=True)

        # Clear off the search results of previous keyword to avoid duplication
        google_news.clear()

    shape = articles.shape[0]
    # Resetting the index of the final result
    articles.index = np.arange(shape)

    # Apply function to 'Articles' column
    # analyse_sentiment function will return the sentiment of the article title
    # summarize_article function will return the summary of the article
    try:
        articles['Sentiment'] = articles['Title'].apply(analyse_sentiment)
        articles['Summary'] = articles['Link'].apply(summarize_article)
    except Exception as e:
        print(f"An error occurred while processing the articles: {e}")

    # Specify the full path to the file
    file_path = "headline.csv"

    # Use a context manager to save the DataFrame to a CSV file
    try:
        with open(file_path, 'w') as f:
            articles.to_csv(f, index=False)
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")


    # # Apply function to 'Articles' column
    # articles['Sentiment'] = articles['Title'].apply(analyse_sentiment)
    # articles['Summary'] = articles['Link'].apply(summarize_article)


    # # Saving fetched articles to excel sheet
    # articles.to_csv('headline.csv', index=False)

if __name__ == '__main__':
    main()
