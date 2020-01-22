import oauth2
import json
import urllib.parse
import pprint


# Credetials Variables resposible for access to the Twitter API
consumer_key = 'XLs018zjJ3C26e6shqPx6ngWF'
consumer_secret = 'sPqVNFtEvub9wlWX0xhJS4sA1dcng1X4hTdPu9vlLSkzCOIzDE'
token = '1184663497675816962-wYDOSSHC9scImvnAcOg9CLMWjHAzHk'
token_secret = '1XB6jkhgFLaajm66fNtm0RzDginGqXKcmcB7P4clwn0Si'

# Creating the client
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token, token_secret)
client = oauth2.Client(consumer, token)

##################################################################################

query = input("What do you want to tweet: ")
#request = client.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query)
query_codificada = urllib.parse.quote(query, safe='')
request = client.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='post' )


decode = request[1].decode()
tweet = json.loads(decode)


