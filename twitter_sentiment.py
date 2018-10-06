
import tweepy
from textblob import TextBlob


consumer_key= 'j9uaFDBqKdmup0u3o5QdnffCB'
consumer_secret= 'wc6N0d4QJmEG114DARhq4ZSPkZEyvmngMfiBHDAqL889YF3LG6'

access_token='282590292-edk45KVNlNhNCxLfLbeJwO1iIpXBmmwybPO728K4'
access_token_secret='V3KYX4PLpFRds6g1OC4Mc4cz81yF5eLmlZX6kFiBg8Yi6'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search('Hazard')






for tweet in public_tweets:
    print(tweet.text)
    
   
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")