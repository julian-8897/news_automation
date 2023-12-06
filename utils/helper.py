import pandas as pd
from typing import Dict, List


def newsfeed(article_info: pd.DataFrame, raw_dictionary: List[Dict]) -> pd.DataFrame:
    """Fetching google search results and storing into DataFrame

    Args:
        article_info (pd.DataFrame): Empty DataFrame with columns
        raw_dictionary (List[Dict]): Containing information for the search results

    Returns:
        pd.DataFrame : pandas DataFrame object containing article information
    """
    for i in range(len(raw_dictionary)-1):
        if raw_dictionary is not None:
            # Fetch the date and time and convert it into datetime format
            date = raw_dictionary[i]['datetime']
            date = pd.to_datetime(date)
            # Fetch the title, time, description and source of the news articles
            title = raw_dictionary[i]['title']
            time = raw_dictionary[i]['date']
            articles = raw_dictionary[i]['desc']
            link = raw_dictionary[i]['link']
            # Append all the above information in a single dataframe
            new_row = pd.DataFrame({'Date': date, 'Time': time, 'Title': title,
                                    'Articles': articles, 'Link': link}, index=[0])
            article_info = pd.concat([article_info, new_row], ignore_index=True)
        else:
            break

    return article_info
