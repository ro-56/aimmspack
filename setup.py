# !/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

NAME = 'aimmspack'
VERSION = '1.0.0'
DESCRIPTION = 'A simple project to automate the creation of .aimmspack packages from a config file.'
URL = 'https://github.com/me/myproject'
AUTHOR = 'Rodrigo Mendonça'
AUTHOR_EMAIL = 'author@example.com'
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
LICENSE = 'MIT'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    license = LICENSE,
    classifiers=[
        'Development Status :: 1 - Planning',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

    package_dir={'aimmspack': 'aimmspack'},

    packages=[
        'aimmspack',
        'aimmspack\\api',
        'aimmspack\\_lib'
        ], 

    python_requires='>=3.9, <4',

    entry_points={
        'console_scripts': [
            'aimmspack=aimmspack.__main__:main',
        ],
    }
)