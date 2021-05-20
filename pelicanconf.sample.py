#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Imports

# These two lines are needed to make sure utils directory is imported
from os.path import join
import sys
sys.path.append('.')

from datetime import datetime
from utils import filters

# Basic Setup
SITENAME = 'Twenty Theme'
TAGLINE = 'Ported for Pelican'
SITEURL = ''
AUTHOR = 'author'
DEFAULT_LANG = 'en'                                 # English
COPYRIGHT_YEAR = datetime.now().strftime('%Y')
DEFAULT_DATE_FORMAT = '%d/%b/%Y'
BANNER = "images/banner.jpg"
BANNER_SUBTITLE = 'Ported for Pelican'
INDEX_INTRODUCTION = 'includes/index_introduction.html'

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images', 'extra', 'docs']
PLUGIN_PATHS = ['plugins']
THEME_STATIC_DIR = 'theme'

CUSTOM_CSS = 'css/custom.css'
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': join(THEME_STATIC_DIR, CUSTOM_CSS) },
    BANNER: {'path': join(THEME_STATIC_DIR, 'images/banner.jpg') }
}

# URLs
ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHORS_SAVE_AS = ''                # Don't need this generated
AUTHOR_SAVE_AS = ''                 # Don't need this generated
ARCHIVES_URL = 'archives'
SEARCH_URL = SITEURL + '/search'

# Plugins
PLUGINS = ['pelican.plugins.tag_cloud', 'pelican.plugins.tipue_search', 'pelican.plugins.share_post', 'pelican.plugins.neighbors']

# Other Pelican Configuration
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_CATEGORIES_AS_SUBMENU = True
CATEGORY_SUBMENU_TITLE = 'Submenu'
DEFAULT_PAGINATION = 3
DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'archives', 'search']
PAGINATED_TEMPLATES = {'index': 3, 'category': 5, 'archives': 5, 'tag': 5, 'author': 5}
MENU_SPECIAL_BUTTON_LABEL = ('Special', '#')

DELETE_OUTPUT_DIRECTORY = False

# Comments
COMMENTS_ENABLED = False
STATICMAN_FORM_ACTION = 'https://<heroku_staticman_app_url>/v3/entry/github/<github_user>/<github_repo>/<branch>/comments'


# Jinja2 Filters
JINJA_FILTERS = {
    'sidebar': filters.sidebar,
    'datediff': filters.datediff
}

# Theme Configuration
THEME = 'theme/twenty'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)


# Social
# The name of the link is used to get the corresponding Font-Awesome icon. Icon-styling is in main.css of theme
SOCIAL = (
    ('twitter', '#'),
    ('linkedin', '#'),
    ('envelope', '#'),
)

# Top Menu Items
MENUITEMS = (
    ('Menu Item1', '#'),
    ('Menu Item2', '#'),
)

# Tag Cloud Configuration
TAG_CLOUD_STEPS = 4	                    # Count of different font sizes in the tag cloud.
TAG_CLOUD_MAX_ITEMS = 20	            # Maximum number of tags in the cloud.
TAG_CLOUD_SORTING = 'alphabetically'	# random, alphabetically, alphabetically-rev, size, size-rev
TAG_CLOUD_BADGE = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True