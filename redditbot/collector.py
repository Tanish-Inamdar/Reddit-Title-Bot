import os
import praw
import pickle
from dotenv import load_dotenv
load_dotenv()

#all of these Rthings are from the .env file from your reddit bot
reddit_instance = praw.Reddit(
    client_id = os.getenv('Rclient_id'),
    client_secret= os.getenv('Rclient_secret'),
    username= os.getenv('Redusername'), 
    password= os.getenv('Redpass'),
    user_agent="test_bot",
)



# reddit post that the comments are being drawn from
submission = reddit_instance.submission('18tcs90')

commentsR = list(submission.comments)

with open('comments.pkl', 'wb') as f:
    pickle.dump(commentsR, f)
 
