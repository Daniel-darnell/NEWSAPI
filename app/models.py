class Sources:
    
    '''
    A Sources class that defines the Sources objects
    '''

    def __init__(self, id, name, description, url, category, country, language):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language


class Articles:

    '''
    An Articles class that defines the articles objects
    '''

    def __init__(self, title,descripion, url, urlToImage, publishedAt):
        self.title = title 
        self.descripion = descripion
        self.url =url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt