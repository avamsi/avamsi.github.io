AUTHOR = 'Vamsi'
SITENAME = "Vamsi's Blog"
SITEURL = ''

DEFAULT_LANG = 'en'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_DATE = 'fs'
SLUGIFY_SOURCE = 'basename'

DEFAULT_PAGINATION = 5

PATH = 'content'

ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['static']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search']

DIRECT_TEMPLATES = ['index', 'archives', 'search']
SEARCH_URL = '/search'

DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'yeti-custom'
CUSTOM_CSS = 'static/custom.css'

TYPOGRIFY = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True

PYGMENTS_STYLE = 'native'

ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'

AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''

FAVICON = 'static/images/favicon.ico'
# SITELOGO = 'static/images/favicon.ico'

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

SOCIAL = [
    ['Github', 'https://github.com/avamsi'],
    ['Facebook', 'https://www.facebook.com/100003243723298'],
    ['Twitter', 'https://twitter.com/_avamsi']
]

LINKS = [
    ['Resume', 'https://drive.google.com/open?id=0B4Sh2RFUjcHhNnIzbUQ2Yno3UG8'],
    ['HackerRank', 'https://www.hackerrank.com/avamsi'],
    ['Codeforces', 'http://codeforces.com/profile/avamsi']
]

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
