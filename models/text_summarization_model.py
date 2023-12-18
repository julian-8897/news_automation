from transformers import pipeline

class TextSummarizationModel:
    def __init__(self):
        self.model = pipeline('summarization', model="Falconsai/text_summarization")
    
    def summarize(self, text, max_length=150, min_length=30, do_sample=False):
        return self.model(text, max_length=max_length, min_length=min_length, do_sample=do_sample)[0]['summary_text']

def create_text_summarization_model():
    return TextSummarizationModel()