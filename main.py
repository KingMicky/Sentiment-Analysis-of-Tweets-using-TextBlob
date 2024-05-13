import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# Read data from CSV file
def read_data(filepath):
    data = pd.read_csv(filepath)
    data['text'] = data['text'].astype(str)
    return data

# Perform sentiment analysis on tweets
def analyze_sentiment(data):
    data['polarity'] = data['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    data['subjectivity'] = data['text'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    data['sentiment'] = data['polarity'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))
    return data

# Visualize sentiment analysis results
def visualize_sentiment(data):
    sns.histplot(data['polarity'], kde=False, color='#539caf')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Count')
    plt.title('Sentiment Analysis Histogram')
    plt.axvline(0, color='gray', linestyle='--')
    plt.show()

# Output sentiment analysis results to markdown table
def output_results(data):
    print("| Text | Polarity | Subjectivity | Sentiment |")
    print("| --- | --- | --- | --- |")
    for index, row in data.iterrows():
        print(f"| {row['text']} | {row['polarity']} | {row['subjectivity']} | {row['sentiment']} |")

# Main function
def main(filepath):
    data = read_data(filepath)
    data = analyze_sentiment(data)
    visualize_sentiment(data)
    output_results(data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python sentiment_analysis.py tweets.csv")
        sys.exit(1)
    filepath = sys.argv[1]
    main(filepath)