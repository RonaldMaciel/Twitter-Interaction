import oauth2
import json
import urllib.parse
import pprint
from datetime import datetime

today = datetime.now()
date_formated = today.strftime(" %d/%m/%Y - %H:%M:%S")

# Credentials Variables responsible for access to the Twitter API
consumer_key = 'XLs018zjJ3C26e6shqPx6ngWF'
consumer_secret = 'sPqVNFtEvub9wlWX0xhJS4sA1dcng1X4hTdPu9vlLSkzCOIzDE'
token_key = '1184663497675816962-wYDOSSHC9scImvnAcOg9CLMWjHAzHk'
token_secret = '1XB6jkhgFLaajm66fNtm0RzDginGqXKcmcB7P4clwn0Si'

# Creating the client
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
client = oauth2.Client(consumer, token)

##################################################################################



