import pandas as pd


def newsfeed(article_info, raw_dictionary):
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
            article_info = article_info.append({'Date': date, 'Time': time, 'Title': title,
                                                'Articles': articles, 'Link': link}, ignore_index=True)
        else:
            break

    return article_info
