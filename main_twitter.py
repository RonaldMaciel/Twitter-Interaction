from twitter_lib import Twitter

# Credentials Variables responsible for access to the Twitter API
consumer_key = 'XLs018zjJ3C26e6shqPx6ngWF'
consumer_secret = 'sPqVNFtEvub9wlWX0xhJS4sA1dcng1X4hTdPu9vlLSkzCOIzDE'
token_key = '1184663497675816962-wYDOSSHC9scImvnAcOg9CLMWjHAzHk'
token_secret = '1XB6jkhgFLaajm66fNtm0RzDginGqXKcmcB7P4clwn0Si'

# Object of the type 'Twitter'
twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

############################### POST/TWEETING ###############################
# .tweet have only 1 argument: your tweet
# Example:
# twitter.tweet('THIS IS A TWEET-EXAMPLE')

############################### SEARCH ###############################
# .search have 2 arguments: the topic you want to search and the language you want then
# Example:
# twitter.search('iran', 'pt')

search = twitter.search('iran', 'pt')

for result in search:
    print(result['user']['screen_name'])
    print(result['text'])
    print()
