# News Automation

This project uses the Google News Python API to fetch and analyze news articles. It includes features for sentiment analysis and text summarization.

## Installation

Clone the repository and install the required Python packages:

```sh
git clone https://github.com/julian-8897/news_automation.git
cd news_automation
pip install -r requirements.txt
```

## Usage

You can fetch news articles by running the automate.py script with command-line arguments for the date range, keywords, and number of pages to fetch:

```sh
python automate.py --lower_date '10/28/2022' --upper_date '10/30/2022' --key_words 'NBA' 'Artificial Intelligence' 'Manchester United' --n_pages 1
```

Running the script will save the fetched results to a 'headlines.csv' file in the current directory.

## Command-line Options

You can customize the command-line options to get a specific date range, keywords or number of pages to be fetched.

```sh
--lower_date (Lower bound of the date range)
--upper_date (Upper bound of the date range)
--key_words (One or more key words to be searched)
--n_pages (Number of pages to be fetched)

```

## Sentiment Analysis

A simple pipeline to analyze the sentiment of article titles is now included. This was achieved using the Transformers API https://huggingface.co/docs/transformers/index.

## Article Summarization

Now supports summarizing of articles using the fine-tuned T5 small model (https://huggingface.co/Falconsai/text_summarization). This can be achieved by running the main script automate.py or running it as an web app on the local server using app.py
