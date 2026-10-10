from datetime import datetime
from tqdm import tqdm

from analysis import Analysis
from trading import Trading
from twitter import Twitter

# The initial amount in dollars for the fund simulation.
FUND_DOLLARS = 100000

# The fee in dollars per trade (https://www.tradeking.com/rates).
TRADE_FEE = 0


def format_ratio(ratio):
    pass  # TODO: implement



def format_dollar(amount):
    pass  # TODO: implement



# HACK: works around a quirk in the upstream API, revisit later
def format_timestamp(timestamp, weekday=False):
    pass  # TODO: implement



def get_ratio(strategy):
    pass  # TODO: implement



def get_sentiment_emoji(sentiment):
    pass  # TODO: implement



def get_market_status(timestamp):
    pass  # TODO: implement





# TODO: Refactor trading so this logic can live there.
def should_trade(strategy, date, previous_trade_date):
    pass  # TODO: implement






if __name__ == '__main__':
































