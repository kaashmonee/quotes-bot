import praw
import pprint

class OCRBot:

    def __init__(self):
        self.reddit = praw.Reddit("bot1")
        self.subreddit = self.reddit.subreddit("quotesporn")

    def run_bot(self):
        # Getting top 5 hot posts
        for submission in self.subreddit.hot(limit=5):
            image_url = submission.url
            ocr_text = self.do_OCR(image_url)
            self.comment_on_post(ocr_text)
            print("image url:", image_url)

            break

    def do_OCR(self, image_url):
        pass
    
    def comment_on_post(self, ocr_text):
        pass

def main():
    bot = OCRBot()
    bot.run_bot()

if __name__ == "__main__":
    main()