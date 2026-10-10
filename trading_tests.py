from datetime import datetime
from pytest import fixture
from pytz import utc

from trading import Trading
from trading import MARKET_TIMEZONE
from trading import TRADEKING_CONSUMER_KEY
from trading import TRADEKING_CONSUMER_SECRET
from trading import TRADEKING_ACCESS_TOKEN
from trading import TRADEKING_ACCESS_TOKEN_SECRET
from trading import TRADEKING_ACCOUNT_NUMBER
from trading import USE_REAL_MONEY


@fixture
def trading():
    pass  # TODO: implement


def as_market_time(year, month, day, hour=0, minute=0, second=0):
    pass  # TODO: implement



def test_environment_variables():
    pass  # TODO: implement


def test_get_strategy_blacklist(trading):
    pass  # TODO: implement


def test_get_strategy_market_status(trading):
    pass  # TODO: implement


def test_get_strategy_sentiment(trading):
    pass  # TODO: implement


def test_get_budget(trading):
    pass  # TODO: implement


def test_utc_to_market_time(trading):
    pass  # TODO: implement


def test_market_time_to_utc(trading):
    pass  # TODO: implement


def test_make_request_success(trading):
    pass  # TODO: implement


def test_make_request_fail(trading):
    pass  # TODO: implement


def test_fixml_buy_now(trading):
    pass  # TODO: implement


def test_fixml_sell_eod(trading):
    pass  # TODO: implement


def test_fixml_short_now(trading):
    pass  # TODO: implement


def test_fixml_cover_eod(trading):
    pass  # TODO: implement


def test_get_buy_limit(trading):
    pass  # TODO: implement


def test_get_sell_limit(trading):
    pass  # TODO: implement


def test_get_balance(trading):
    pass  # TODO: implement


def test_get_last_price(trading):
    pass  # TODO: implement


def test_get_market_status(trading):
    pass  # TODO: implement


def test_get_order_url(trading):
    pass  # TODO: implement


def test_get_quantity(trading):
    pass  # TODO: implement


def test_get_historical_prices_1(trading):
    pass  # TODO: implement


def test_get_historical_prices_2(trading):
    pass  # TODO: implement


def test_get_historical_prices_3(trading):
    pass  # TODO: implement


def test_get_historical_prices_4(trading):
    pass  # TODO: implement


def test_get_historical_prices_5(trading):
    pass  # TODO: implement


def test_get_historical_prices_6(trading):
    pass  # TODO: implement


def test_get_historical_prices_7(trading):
    pass  # TODO: implement


def test_get_historical_prices_8(trading):
    pass  # TODO: implement


def test_get_historical_prices_9(trading):
    pass  # TODO: implement


def test_get_historical_prices_10(trading):
    pass  # TODO: implement


def test_get_historical_prices_11(trading):
    pass  # TODO: implement


def test_get_historical_prices_12(trading):
    pass  # TODO: implement


def test_get_historical_prices_13(trading):
    pass  # TODO: implement


def test_get_historical_prices_14(trading):
    pass  # TODO: implement


def test_get_historical_prices_15(trading):
    pass  # TODO: implement


def test_get_historical_prices_16(trading):
    pass  # TODO: implement


def test_get_historical_prices_17(trading):
    pass  # TODO: implement


def test_get_historical_prices_18(trading):
    pass  # TODO: implement


def test_get_historical_prices_19(trading):
    pass  # TODO: implement


def test_get_historical_prices_20(trading):
    pass  # TODO: implement


def test_get_historical_prices_21(trading):
    pass  # TODO: implement


def test_get_historical_prices_22(trading):
    pass  # TODO: implement


def test_get_day_quotes(trading):
    pass  # TODO: implement


def test_is_trading_day(trading):
    pass  # TODO: implement


def test_get_previous_day(trading):
    pass  # TODO: implement


def test_get_next_day(trading):
    pass  # TODO: implement


def test_make_order_request_success(trading):
    pass  # TODO: implement


def test_make_order_request_fail(trading):
    pass  # TODO: implement


def test_bull(trading):
    pass  # TODO: implement


def test_bear(trading):
    pass  # TODO: implement


def test_make_trades_success(trading):
    pass  # TODO: implement


def test_make_trades_fail(trading):
    pass  # TODO: implement
