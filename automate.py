import pandas as pd
import numpy as np
import argparse
from GoogleNews import GoogleNews
from utils.helper import newsfeed

parser = argparse.ArgumentParser()
parser.add_argument('--lower_date',
                    type=str,
                    help='Lower bound for date range',
                    default='10/28/2022')

parser.add_argument('--upper_date',
                    type=str,
                    help='Upper bound for date range',
                    default='10/30/2022')

parser.add_argument('--key_words',
                    nargs='+',
                    help='List of Search Keywords',
                    required=True)

parser.add_argument('--n_pages',
                    type=int,
                    help='Specified number of pages to fetch articles',
                    default=1)

args = parser.parse_args()

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

    articles = articles.append(feed)

    # Clear off the search results of previous keyword to avoid duplication
    google_news.clear()

shape = articles.shape[0]
# Resetting the index of the final result
articles.index = np.arange(shape)

# Saving fetched articles to excel sheet
articles.to_excel('headline.xlsx')
