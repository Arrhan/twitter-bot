import tweepy
import time

#authentication for twitter API - Add relevant twitter access tokens
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')
api = tweepy.API(auth)

#display your twitter timeline
public_tweets=api.home_timeline()
for tweets in public_tweets:
    print(tweets.text)

#info about user
user=api.me()
print(user.followers_count)

#making sure twitter limit rate not exceeded - limit rate is there to make sure our program does not overwork/break their servers
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

#Liking and retweeting posts for a specifc search query
search_query="Python"
number_tweets=2

for tweet in tweepy.Cursor(api.search, search_query).items(number_tweets): #Dont neeed limit handler as we only have 2 items to loop through
    try:
        tweet.favorite()
        tweet.retweet()
        print("Interesting tweet")
    except StopIteration:
        break
    except tweepy.TweepError as e:
        print(e.reason)


#Following back someone you follow
for follower in limit_handler(tweepy.Cursor(api.followers).items()): #Loops through all the people who follow you, items() allows us to loop through it
    print(follower.name)
    follower.follow()