import logging
import praw
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import threading

PRAW_CLIENT_ID ="MhGsIxv8rghQ0Q"
PRAW_CLIENT_SECRET = "d55OpECjc3c0ZJXZnFMgZmnLQGWUoQ"
PRAW_USERAGENT = "erun bot V1.0 by /u/e_run_pie"


reddit = praw.Reddit(client_id=PRAW_CLIENT_ID,
                     client_secret=PRAW_CLIENT_SECRET,
                     user_agent=PRAW_USERAGENT)


def get_memes_urls():

    req_subreddits = ["memes", "dankmemes" ,"MemeEconomy" , "ComedyCemetery","PrequelMemes","dankvideos","youtubehaiku"]  # subreddits
    meme_list = []
    for req_subreddit in req_subreddits:
        subreddit = reddit.subreddit(req_subreddit)
        for submission in subreddit.hot():
            meme_list.append(
                ["https://reddit.com" + submission.permalink, submission.title, submission.url])


    random.shuffle(meme_list)  # to shuffle obtained posts
    return meme_list[:1]


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



event = threading.Event()


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('pls do not start the this is not for public use >')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('pls do not start the this is not for public use >')

def meme(update: Update, context: CallbackContext):
  while True :
    url_caption_list = get_memes_urls()
    for url_caption in url_caption_list:
        url = url_caption[0]
        img_url = url_caption[2]
        img_caption = url_caption[1]
        context.bot.send_photo(chat_id='@redditmemee', photo = img_url, caption = img_caption +'\nSource : ' + url +'\n- @redditmemee -' )
    event.wait(900)
def main():

    updater = Updater("1716073347:AAEqs18P2-oe5oPWVmzUMdpX_RbZMJQeAAw")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start , run_async=True ))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("memesecret", meme, run_async=True))

    updater.start_polling()

    updater.idle()


    meme()

if __name__ == '__main__':
    main()
