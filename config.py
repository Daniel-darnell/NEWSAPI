import os 

class Config:

    '''
    General parent configuration class
    '''

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_SOURCES_BASE_URL = ''
    ARTICLES_BASE_URL = ''
    SECRET_KEY = os.environ.get('')


class ProdConfig(Config):

    '''
    a child production configuration class
    '''

    pass


class DevConfig(Config):

    '''
    A child developmenmt configuration class
    '''

    pass


config_options = {
    'developmeny': DevConfig,
    'production' : ProdConfig
}