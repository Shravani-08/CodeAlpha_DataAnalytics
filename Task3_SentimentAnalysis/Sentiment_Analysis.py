import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Sample review dataset
reviews = { 
    "review": [
        "This movie was amazing and very inspiring",
        "Worst show I have ever watched",
        "It was okay, nothing special",
        "Absolutely loved the storyline and acting",
        "Terrible experience, boring plot",
        "Good cinematography and decent acting",
        "Not bad but could be better"
    ]
}

df = pd.DataFrame(reviews)

# Function for sentiment classification
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["review"].apply(get_sentiment)

# Print results
print("=" * 50)
print("SENTIMENT ANALYSIS RESULTS")
print("=" * 50)
print(df)

# Plot graph
df["Sentiment"].value_counts().plot(kind="bar", figsize=(8, 5))
plt.title("Sentiment Analysis of Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()