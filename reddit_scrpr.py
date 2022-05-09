import praw
import pandas as pd
from praw.models import MoreComments

import pandas as pd



def get_posts_hot(reddit, sub, limit=100):
    
    ml_subreddit = reddit.subreddit(sub)   
    
    posts=[]
    for post in ml_subreddit.hot(limit=limit):
    # for post in ml_subreddit.popular(limit=100):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    
    posts_df = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    
    return posts_df

def get_post_comments(reddit, post_id):
    
    submission = reddit.submission(id=post_id)
    submission.comments.replace_more(limit=None)
    
    # comments_list = submission.comments.list()

    result_df = pd.DataFrame()
    cols=['comment_id','parent_id','created','body']
    # cols=['comment_id','parent_id','created']
    
    for comment in submission.comments.list():

        df=pd.DataFrame([[comment.id,str(comment.parent()),int(comment.created_utc),comment.body]],columns=cols)
        result_df = result_df.append(df,ignore_index=True)
        
        # df=pd.DataFrame([[comment.id,str(comment.parent()),int(comment.created_utc)]],columns=cols)
        # result_df = result_df.append(df,ignore_index=True)
        
    return result_df

    
def get_posts_comments_hot(reddit, sub, limit=100):
    
    conps_hot_posts = get_posts_hot(reddit, sub,limit=limit)
    result_df = pd.DataFrame()
    
    for post_id in conps_hot_posts['id']:
        print(post_id)
        df = get_post_comments(reddit, post_id)
        df['post_id'] = str(post_id)
        result_df = result_df.append(df, ignore_index=True)
        
    return result_df

def main():
    
    path = '/path/to/'

    
    reddit = praw.Reddit(client_id='', client_secret='', user_agent='', check_for_async=False)
    
    sub = 'Conspiracy'

    consp_hot_posts = get_posts_hot(reddit, sub,limit=20)
    consp_hot_posts.shape

    i=1
    post_id=consp_hot_posts['id'][i]
    
    post_comments_df = get_post_comments(reddit, post_id)
    post_comments_df.shape
    
    all_post_comments_df = get_posts_comments_hot(reddit, sub, limit=3)
    all_post_comments_df.shape
    
    all_post_comments_df.to_csv(path+'allcom3.csv')
    
if __name__ == "__main__":
        main() 
