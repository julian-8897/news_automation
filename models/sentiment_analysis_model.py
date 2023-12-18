from transformers import pipeline

class SentimentAnalysisModel:
    def __init__(self):
        self.nlp_model = pipeline('sentiment-analysis')

    def apply_model(self, article):
        return self.nlp_model(article)[0]

def create_sentiment_analysis_model():
    return SentimentAnalysisModel()