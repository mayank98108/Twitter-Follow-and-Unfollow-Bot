import tweepy
import json
from time import sleep
from re import search
from itertools import cycle
from random import shuffle

# gets all of our data from the config file.
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

screen_name = config_data["auth"]["screen_name"]

# authorization from values inputted earlier, do not change.
auth = tweepy.OAuthHandler(config_data["auth"]["CONSUMER_KEY"], config_data["auth"]["CONSUMER_SECRET"])
auth.set_access_token(config_data["auth"]["ACCESS_TOKEN"], config_data["auth"]["ACCESS_SECRET"])
api = tweepy.API(auth)


# search for the tweets

userList = []

for i in api.search_users("follow back",count=10):
	userList.append(i._json["screen_name"])

#print(userList)

total_followed = 0
# starts following users.
for f in userList:
    try:
        api.create_friendship(f)
        total_followed += 1
        if total_followed % 10 == 0:
            print(str(total_followed) + ' users followed so far.')
        print('Followed user. Sleeping 180 seconds.')
        sleep(180)
    except (tweepy.RateLimitError, tweepy.TweepError) as e:
        error_handling(e)
print(total_followed)
#userList = api.search_users("follow back")._json["screen_name"]
#print(api.me()._json["screen_name"])

