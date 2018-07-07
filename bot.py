import praw
import pprint


def main():
    reddit = praw.Reddit("bot1")
    subreddit = reddit.subreddit("quotesporn")

    # Getting top 5 hot posts
    for submission in subreddit.hot(limit=5):
        pprint.pprint(vars(submission))
        image_url = submission["url"]
        ocr_text = do_ocr(image_url)
        comment_on_post(ocr_text)

        break


def do_OCR(image_url) -> str:
    pass

def comment_on_post(ocr_text):
    pass

if __name__ == "__main__":
    main()