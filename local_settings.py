'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'gFrsipzfT4vtFWt63xqidpAxA'
MY_CONSUMER_SECRET = 'gLeLQ53ykObJqWAHQnbisizd8GPlzr5cwW9II3yM7IZjCo524j'
MY_ACCESS_TOKEN_KEY = '	899617065375608832-aLNvrdAgFitNyh7S1elnsINQJqWoJQ4'
MY_ACCESS_TOKEN_SECRET = 'nT4R2m2cE0ApjxDu83gEObeaYySelIjp0OrNfT6S9jW99'

SOURCE_ACCOUNTS = ["TheHockeyNews"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 4 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = True #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "HockeyNewsBot" #The name of the account you're tweeting to.
