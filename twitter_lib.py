import oauth2
from _datetime import datetime
import urllib.parse
import json

class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.link(consumer_key, consumer_secret, token_key, token_secret)


    def link(self, consumer_key, consumer_secret, token_key, token_secret):
        # Creating the client
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.client = oauth2.Client(self.consumer, self.token)

    def tweet(self, new_tweet):
        #query = input("What do you want to tweet: ")
        # request = client.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query)
        query_codified = urllib.parse.quote(new_tweet, safe='')
        request = self.client.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codified,
                                 method='POST')
        decode = request[1].decode()
        tweet = json.loads(decode)

        return tweet

    def search(self, query, lang):
        query_codified = urllib.parse.quote(query, safe='')
        request = self.client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codified + '&lang=' + lang)
        decode = request[1].decode()
        search = json.loads(decode)

        decoded_search = search['statuses']
        return decoded_search




