import tweepy
import time
import random
#you need to enter your own credentials :)
auth = tweepy.OAuthHandler('*******************','*************')
auth.set_access_token('*************','****************************')

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user=api.me()

search= '#rgpv_spreading_corona_virus'
nrTweet=500

for tweet in tweepy.Cursor(api.search,search).items(nrTweet):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
        n = random.randint(1,4)
        time.sleep(n)
    except tweepy.TweepError as e:
        print (e.reason)
    except StopIteration:
        break    





