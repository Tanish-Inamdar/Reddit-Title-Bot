import os
import praw
import pickle
from dotenv import load_dotenv
load_dotenv()


reddit_instance = praw.Reddit(
    client_id = os.getenv('Rclient_id'),
    client_secret= os.getenv('Rclient_secret'),
    username= os.getenv('Redusername'), 
    password= os.getenv('Redpass'),
    user_agent="test_bot",
)




submission = reddit_instance.submission('18tcs90')

commentsR = list(submission.comments)

with open('comments.pkl', 'wb') as f:
    pickle.dump(commentsR, f)
 
