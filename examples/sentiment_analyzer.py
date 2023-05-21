import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

sia = SentimentIntensityAnalyzer()

text = "I love this movie! But the acting was mediocre, sadly."

sentences = sent_tokenize(text)

# Analyse de sentiment pour chaque phrase
total_compound = 0
for sentence in sentences:
    sentiment_scores = sia.polarity_scores(sentence)
    print(f"Sentence: {sentence}")
    print(f"Sentiment scores: {sentiment_scores}")
    total_compound += sentiment_scores['compound']

print(f"Sentiment score de la phrase : {total_compound / len(sentences):.3}")
