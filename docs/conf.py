import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'KeePass Login Account'
author = 'Documentation Team'
release = '1.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

html_baseurl = 'https://password-manager-guides.readthedocs.io/en/latest/'

html_static_path = ['_static']

html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False

html_extra_path = ['robots.txt', 'sitemap.xml']

# Google & Bing Verification Meta Tags
html_context = {
    "meta_tags": """
    <meta name="google-site-verification" content="Cva8KgvW-eQpRtsdf8vIcSb023IJtLJfC8PxJAlQ0mc" />
    <meta name="msvalidate.01" content="739245F5D54BCBF40AC056DC0CBF5710" />
    """
}
