# -*- coding: utf-8 -*-

"""
Created on 2013-02-24
:author: Andreas Kaiser (disko)
"""
from __future__ import absolute_import

from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery


library = Library('fineuploader', 'resources')

fineuploader_css = Resource(
    library,
    'fine-uploader/fine-uploader.css',
    minified='fine-uploader/fine-uploader.min.css')

fineuploader = Resource(
    library,
    'fine-uploader/fine-uploader.js',
    minified='fine-uploader/fine-uploader.min.js')

jquery_fineuploader = Resource(
    library,
    'jquery.fine-uploader/jquery.fine-uploader.js',
    minified='jquery.fine-uploader/jquery.fine-uploader.min.js',
    depends=[jquery])
