# -*- coding: utf-8 -*-

"""
Created on 2013-02-24
:author: Andreas Kaiser (disko)
"""

import os

from setuptools import find_packages
from setuptools import setup


version = '3.3.0'


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
    classifiers=[],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binarypunks.com',
    url='https://github.com/disko/js.fineuploader',
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
    )
