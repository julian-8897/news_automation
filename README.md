## Description

Personalized news automation using Google News Python API :https://pypi.org/project/GoogleNews/.

## Installation Guide

```
$ git clone https://github.com/julian-8897/news_automation.git
$ cd news_automation
$ pip install -r requirements.txt
```

## How to use

In order to fetch the news articles, run the following example command:

```
python automate.py --lower_date '10/28/2022' --upper_date '10/30/2022' --key_words 'NBA' 'Artificial Intelligence' 'Manchester United' --n_pages 1
```

Running the script will save the fetched results to a headlines.xlsx' excel file in the current directory.

## Command-line Options

You can customize the command-line options to get a specific date range, keywords or number of pages to be fetched.

```
--lower_date (Lower bound of the date range)
--upper_date (Upper bound of the date range)
--key_words (One or more key words to be searched)
--n_pages (Number of pages to be fetched)
```
