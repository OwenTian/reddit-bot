'''

PRAW - wrapper for reddit API, makes accessing reddit a lot easier

'''

import praw
import config
import time

def bot_login():
	print "Logging in..."
	r = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "fluttertest's occultist heal responder")

	return r

def run_bot(r):
	print "Obtaining comments"
	for comment in r.subreddit('test').comments(limit=25):
		if "Wyrd Reconstruction!" in comment.body:
			print "\"Wyrd Reconstruction\" found!"
			print "replied to comment " + comment.id
			comment.reply("CRIT! 0. Bleed.")

	print "Sleeping for 10 seconds"
	time.sleep(10)

r = bot_login()
while True:
	run_bot(r)



