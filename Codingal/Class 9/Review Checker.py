#Review Checker
from textblob import TextBlob
review = input ("Enter your review:")
objTextBlob = TextBlob(review)
sentiment = objTextBlob.sentiment.polarity

print("Sentiment:",sentiment)
if sentiment > 0:
    print("You have given a positive review!")
else:
    print("Oops,You have given a negative review!")