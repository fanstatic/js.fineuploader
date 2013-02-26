# -*- coding: utf-8 -*-

"""
Created on 2013-02-24
:author: Andreas Kaiser (disko)
"""

from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery


library = Library('fineuploader', 'resources')

fineuploader_css = Resource(library, 'fineuploader.css')

fineuploader = Resource(
    library,
    'fineuploader.js',
    minified='fineuploader.min.js')
jquery_fineuploader = Resource(
    library,
    'jquery.fineuploader.js',
    minified='jquery.fineuploader.min.js',
    depends=[jquery])
