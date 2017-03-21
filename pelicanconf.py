#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'heiko'
SITENAME = u'openscreencast'
SITEURL = 'http://www.openscreencast.de'

TIMEZONE = 'Europe/Berlin'

TAGLINE = 'Screencasts über Open Source- und freie Software-Anwendungen'

DEFAULT_LANG = u'de'

THEME = "./pelican-svbhack-master"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'blog/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = 'feeds/%s.tag.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.tag.atom.xml'
FEED_ALL_RSS = 'blog/rss.xml'
TRANSLATION_FEED_ATOM = None

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

TAG_URL = 'tag/{slug}tag.html'
TAG_SAVE_AS = 'tag/{slug}tag.html'

DISQUS_SITENAME = 'openscreencast'

# Blogroll
#LINKS =  (('Flickr', 'http://www.flickr.com/photos/redcctshirt'),
#          ('openclipart', 'http://www.openclipart.org/user-detail/redccshirt'),
#          ('tumblr', 'http://redcctshirt.tumblr.com/'),
#	  ('pixabay', 'http://www.pixabay.com/de/users/redcctshirt'),)
LINKS =  (('Videotutorials', 'http://www.openscreencast.de/videotutorials/'),)


# Social widget
#SOCIAL = (('twitter', 'https://twitter.com/redcctshirt'),
#          ('github', 'https://github.com/openscreencast'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
