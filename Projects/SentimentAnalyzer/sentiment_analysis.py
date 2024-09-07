#Sentiment means overall emotional tone or attitude expressed in a piece of text

from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

# Example usage
if __name__ == "__main__":
    text_to_analyze = input("Enter text to analyze sentiment: ")
    sentiment = analyze_sentiment(text_to_analyze)
    print(f"Sentiment: {sentiment}")


#Result
#polarity = emotion (positive or negative)
#objectivity =  it tells how personal or objective the text is.