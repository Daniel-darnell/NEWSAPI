import urllib.request,json
from models import Sources, Articles

#Getting the api key 
api_key = None

#Getting the News base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.cofig['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_base_url = app.config['NEWS_SOURCES_BASE_URL']


