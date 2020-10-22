from flask import render_template, request, redirect, url_for
from .import main
from ..requests import get_sources, get_articles
from ..models import Sources, Articles


#Views
@main.route('/')
def index():

    '''
    A view root function that returns the index page and its data
    '''


    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    technology_sources = get_sources('technology')
    sports_sources = get_sources('sports')
    health_sources = get_sources('health')

    title = "NewsFlash"

    return render_template('index.html', title = title, business_sources=business_sources, sports_sources=sports_sources, health_sources=health_sources, technology_sources=technology_sources, entertainment_sources=entertainment_sources)
