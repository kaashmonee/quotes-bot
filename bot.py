import praw


def main():
    reddit = praw.Reddit("bot1")
    subreddit = reddit.subreddit("quotesporn")

    # Getting top 5 hot posts
    for submission in subreddit.hot(limit=5):
        print("submission:", submission)

if __name__ == "__main__":
    main()