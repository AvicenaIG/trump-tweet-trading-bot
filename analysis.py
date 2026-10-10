from backoff import expo
from backoff import on_exception
from google.cloud import language_v1 as language
from re import compile
from re import IGNORECASE
from requests import get
from requests.exceptions import HTTPError
from urllib.parse import quote_plus

from logs import Logs
from twitter import Twitter

# The URL for a GET request to the Wikidata API. The string parameter is the
# SPARQL query.
WIKIDATA_QUERY_URL = 'https://query.wikidata.org/sparql?query=%s&format=JSON'

# The HTTP headers with a User-Agent used for Wikidata requests.
WIKIDATA_QUERY_HEADERS = {

# A Wikidata SPARQL query to find stock ticker symbols and other information
# for a company. The string parameter is the Freebase ID of the company.
MID_TO_TICKER_QUERY = (

# A Wikidata SPARQL query to find cryptocurrencies and their symbols. The
# string parameter is the Freebase ID of the company.
MID_TO_CRYPTO_QUERY = (


class Analysis:
    pass  # TODO: implement

    def __init__(self, logs_to_cloud):
        pass  # TODO: implement

    def get_company_data(self, mid):
        pass  # TODO: implement














    def find_companies(self, tweet):
        pass  # TODO: implement













    def get_expanded_text(self, tweet):
        pass  # TODO: implement








    def make_wikidata_request(self, query):
        pass  # TODO: implement






    def get_sentiment(self, text):
        pass  # TODO: implement




