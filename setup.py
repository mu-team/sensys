#!/usr/bin/env python

import pathlib
import setuptools


PROJECT_ROOT = pathlib.Path(__file__).parent
README_FILE = (PROJECT_ROOT / 'README.md').as_posix()

with open(README_FILE) as f:
    verbose = f.read()

about = {
    'name': 'sensys',
    'version': '0.1.0',
    'author': 'Kirill (kxnes) Kolesnikov',
    'author_email': 'kkxnes@gmail.com',
    'license': 'The MIT License',
    'url': 'https://github.com/mu-team/sensys'
}

description = {
    'description': 'Python Sen(try) --> Sys(log) workaround.',
    'long_description': verbose,
    'long_description_content_type': 'text/markdown'
}

packages = [
    'sensys.plugin',
    'sensys.contrib.django'
]

requires = [
    'raven>=6.9.0'
]

setuptools.setup(
    **about,
    **description,
    packages=packages,
    install_requires=requires,
    entry_points={
        'console_scripts': ['sensys=sensys.plugin:main']
    },
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
