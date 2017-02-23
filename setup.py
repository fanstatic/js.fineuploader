# -*- coding: utf-8 -*-

"""
Created on 2013-02-24
:author: Andreas Kaiser (disko)
"""

import os

from setuptools import find_packages
from setuptools import setup


version = '5.14.0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'fineuploader', 'test_fineuploader.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.fineuploader',
    version=version,
    description="Fanstatic packaging of Fine Uploader",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
    ],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binarypunks.com',
    url='https://github.com/fanstatic/js.fineuploader',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'fineuploader = js.fineuploader:library',
        ],
    },
    extras_require={
        'testing': ['setuptools-git', 'pytest', 'tox', ],
    },
)
