import oauth2
import json
import urllib.parse
import pprint


# Credentials Variables responsible for access to the Twitter API
consumer_key = 'XLs018zjJ3C26e6shqPx6ngWF'
consumer_secret = 'sPqVNFtEvub9wlWX0xhJS4sA1dcng1X4hTdPu9vlLSkzCOIzDE'
token = '1184663497675816962-wYDOSSHC9scImvnAcOg9CLMWjHAzHk'
token_secret = '1XB6jkhgFLaajm66fNtm0RzDginGqXKcmcB7P4clwn0Si'

# Creating the client
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token, token_secret)
client = oauth2.Client(consumer, token)
#################################################################################

# Creating the request for search
# After the given URL, you can add "?q=brasil" for example, to search for tweets about Brazil
# ?q=Australia, ?q=Iran, ...
# EXAMPLE: request = client.request('https://api.twitter.com/1.1/search/tweets.json?q=brasil')
# But in here, we gonna type what we want to search for
# You can search only in pt-br:
# EXAMPLE: request = client.request('https://api.twitter.com/1.1/search/tweets.json?q= + query + '&lang=pt')
query = input("What are you searching for: ")
request = client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query)
# You can search only in pt-br:
# EXAMPLE: request = client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query + '&lang=pt')


# The query_codificada allows you to search for hashtags, words with specials caracters, á â ã ...
query_codificada = urllib.parse.quote(query, safe='')
# EXAMPLE: request = client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')


# request is a tuple, so we decote to get the first part (text) and eliminate the second part (bytes)
decode = request[1].decode()
tweet = json.loads(decode)


# statuses is the first parametres of an tweet: its a list (dict) that contains every information about a tweet
# the others parametres are just to filter what we want: the text of an tweet
# every index of came after 'statuses' are info about tweets, so we get anyone, like index 0, and get the text of its tweet
# the other parameters can be changed to obtain what we search for like, user, image, favorites, retweets etc
    #pprint.pprint(tweet['statuses'][0]['user']['screen_name'])
    #pprint.pprint(tweet['statuses'][0])

tweets = tweet['statuses']

for twit in tweets:                      # printing some tweets with username
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()

