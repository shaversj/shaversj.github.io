# Theme-specific settings
SITENAME = 'Josh Shavers'
DOMAIN = 'joshshavers.com'
# BIO_TEXT = ''

FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican>.'

SITE_AUTHOR = 'Josh Shavers'
TWITTER_USERNAME = '@JoshShavers'
INDEX_DESCRIPTION = 'Website and blog of Josh Shavers'

SIDEBAR_LINKS = [
    '<a href="/about/">About</a>',
    '<a href="/archive/">Archive</a>',
]

ICONS_PATH = 'images/icons'

SOCIAL_ICONS = [
    ('https://twitter.com/JoshShavers', 'Twitter', 'fa-twitter'),
    ('https://github.com/shaversj', 'GitHub', 'fa-github'),
]

THEME_COLOR = '#FF8000'

# Pelican settings
RELATIVE_URLS = True
SITEURL = 'http://joshshavers.com'
TIMEZONE = 'US/Eastern'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%B %-d, %Y'
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 42

THEME = 'pneumatic'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Disable authors, categories, tags, and category pages
DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TYPOGRIFY = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {'linenums': None},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'develop'
PATH = 'content'

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

STATIC_PATHS = ['images', 'files', 'extra']
IGNORE_FILES = ['.DS_Store', 'pneumatic.scss', 'pygments.css']

SITEIMAGE = '/images/profile.jpeg width=200 height=200'

extras = ['CNAME', 'favicon.ico', 'keybase.txt', 'robots.txt']
EXTRA_PATH_METADATA = {'extra/%s' % file: {'path': file} for file in extras}

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['plugins.assets', 'plugins.neighbors', 'plugins.render_math']
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
    ('cache', False),
    ('manifest', False),
    ('url_expire', False),
    ('versions', False),
]