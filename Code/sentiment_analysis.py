import pandas as pd
from textblob import TextBlob 

def removeNonASCII(string):
    fixed = ''
    for c in string:
        if ord(c) < 128: fixed += c
    return fixed

def get_tweet_sentiment(tweet): 
    ''' 
    Utility function to classify sentiment of passed tweet 
    using textblob's sentiment method 
    '''
    # set sentiment 
    if tweet.sentiment.polarity > 0: 
        return 'positive'
    elif tweet.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'

# Read in the csv; encoding='latin 1' gives pandas the ability to parse the strange characters
tweets = pd.read_csv("/Users/meaghansearles/Documents/GMU/CS504/CASdata-dedoop.csv", encoding='latin 1')
# Make any null values 0
tweets = tweets.fillna(0)
# This loop removes the extra 245 blank rows
for i in range(245):
    tweets = tweets.drop(index=2170+i)
# Removes any of the strange characters
tweets['content'] = tweets.apply(lambda x: removeNonASCII(x['content']), axis=1)

for idx in tweets.index:
    tweet1 = TextBlob(tweets['content'][idx])
    pol = tweet1.sentiment.polarity
    tweets.at[idx, 'polarity'] = pol
    sub = tweet1.sentiment.subjectivity
    tweets.at[idx, 'subjectivity'] = sub

# Finds the index of the tweets that are negative and records in a list
negatives = []
for i in tweets.index:
    if tweets['polarity'][i] < 0.0:
        negatives.append(i)

# Finds the index of the tweets that are positive and records in a list
positives = []
for i in tweets.index:
    if tweets['polarity'][i] > 0.0:
        positives.append(i)

# Finds the index of the tweets that are neutral and records in a list
neutral = []
for i in tweets.index:
    if tweets['polarity'][i] == 0.0:
        neutral.append(i)

# Print negative tweets to a csv
for num in negatives:
    Negative_Tweets = tweets[tweets.polarity < 0.0]
Negative_Tweets.to_csv(path_or_buf='Negative_Tweets.csv', index=False)

# Print positive tweets to a csv
for num in positives:
    Positive_Tweets = tweets[tweets.polarity > 0.0]
Positive_Tweets.to_csv(path_or_buf='Positive_Tweets.csv', index=False)

# Print neutral tweets to a csv
for num in neutral:
    Neutral_Tweets = tweets[tweets.polarity == 0.0]
Neutral_Tweets.to_csv(path_or_buf='Neutral_Tweets.csv', index=False)






