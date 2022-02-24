import tweepy
import random
# import tkinter
import time
import os

def search_requests():
    twt = api.search(q="@randomkittybot !catpic")
    t = ['@randomkittybot !catpic',
         '@randomkittybot ! catpic',
         '@randomkittybot !cat pic']

    for s in twt:
        for i in t:
            if i == s.text:
                sn = s.user.screen_name
                m = api.update_with_media("cat-12.jpg", "@%s" % (sn))
                s = api.update_status(m, s.id)

def post_pics():
    # iterates through images in cat-pics folder
    os.chdir('cat-pics')
    cat_image = random.randint(0, 48)
    for cat_image in os.listdir('.'):
        api.update_with_media(cat_image)
        cat_image = random.randint(0, 48)
        search_requests()
        # tweets an image every hour
        time.sleep(3600)

# credentials for the twitter cat bot
api_key = 'rErzHMxvVBULzbnOsDg1ZlbOx'
api_key_secret = 'JOhy3l5QvczteWQAboxzeA57B0oV2fpxxRr2Do4A8xwNINEIJt'
access_token = '1426382447789416449-7188AtNhvXbdYv10oJgeb2RN1Wo3Uv'
access_token_secret = 'hgn0oKRFLjpLovrCxDKVtJvywgvRawjiRltzMqii255qs'

# login to twitter cat bot api
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# to check if able to successfully login
# user = api.me()
# print(user.name)

post_pics()