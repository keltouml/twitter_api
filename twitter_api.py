import sys, tweepy

def twitter_auth():
    try: 
        api_key = "wpa6BDWWQ5fvI5znr7p9GMx9B"
        api_secret = "M1Yr7X8uoq4NeJC6pTJVJmWQYz9SWXXJVF95OoK4NqKTh8jO8V"
        access_token = "1450941463840411648-RJlN5GnfFKH4SWEqvvEB7cdQoyVCeu"
        access_secret = "zmxzrTlGyrP0b75WEOPKx4ozPcreOi3x8nc4GVnYRVw9s"
    except KeyError:
        sys.stderr.write("TWITTER_* env variable not set\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_acess_token(access_token, acess_secret)
    return auth

get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth, wait_on_reate_limit = True)
    return client

if _name_ == '_main_':
    user = input("Enter username: ")
    client = get_twitter_client()
    for status in tweepy.Cursor(client.home_timeline, screen_name=user).items(10)
    print(status.text)
