'''

PRAW - wrapper for reddit API, makes accessing reddit a lot easier

'''

import praw
import config


def bot_login():
	r = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "fluttertest's occultist heal responder")

	return r

r = bot_login()



