#!/usr/bin/env python
from distutils.core import setup

setup(
    name = 'bambu-pages',
    version = '2.0',
    description = 'Tools for Django webapps',
    author = 'Steadman',
    author_email = 'mark@steadman.io',
    url = 'http://pypi.python.org/pypi/bambu-pages',
    install_requires = [
        'Django>=1.4',
        'bambu-attachments',
        'bambu-markup',
        'bambu-formatrules'
    ],
    namespace_packages = ['bambu'],
    packages = [
        'bambu_pages',
        'bambu_pages.migrations'
    ],
    package_data = {
        'bambu_pages': [
            'templates/pages/*.html',
            'templates/search/indexes/pages/*.txt'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django'
    ]
)
