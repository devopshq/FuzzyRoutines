#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
import os

__version__ = '1.0'  # identify main version of FuzzyRoutines
devStatus = '4 - Beta'  # default build status, see: https://pypi.python.org/pypi?%3Aaction=list_classifiers

if 'TRAVIS_BUILD_NUMBER' in os.environ and 'TRAVIS_BRANCH' in os.environ:
    print("This is TRAVIS-CI build")
    print("TRAVIS_BUILD_NUMBER = {}".format(os.environ['TRAVIS_BUILD_NUMBER']))
    print("TRAVIS_BRANCH = {}".format(os.environ['TRAVIS_BRANCH']))

    __version__ += '.{}{}'.format(
        '' if 'release' in os.environ['TRAVIS_BRANCH'] or os.environ['TRAVIS_BRANCH'] == 'master' else 'dev',
        os.environ['TRAVIS_BUILD_NUMBER'],
    )

    devStatus = '5 - Production/Stable' if 'release' in os.environ['TRAVIS_BRANCH'] or os.environ['TRAVIS_BRANCH'] == 'master' else devStatus

else:
    print("This is local build")
    __version__ += '.dev0'  # set version as major.minor.localbuild if local build: python setup.py install

print("FuzzyRoutines build version = {}".format(__version__))

setup(
    name='fuzzyroutines',

    version=__version__,

    description='FuzzyRoutines library contains some routines for work with fuzzy logic operators, fuzzy datasets and fuzzy scales.',

    long_description='You can see detailed user manual here: https://devopshq.github.io/FuzzyRoutines/',

    license='MIT',

    author='Timur Gilmullin',

    author_email='tim55667757@gmail.com',

    url='https://devopshq.github.io/FuzzyRoutines/',

    download_url='https://github.com/devopshq/FuzzyRoutines.git',

    classifiers=[
        'Development Status :: {}'.format(devStatus),
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],

    keywords=[
        'fuzzy',
        'logic',
        'math',
        'science',
        'research',
        'fuzzylogic',
        'fuzzyset',
    ],

    packages=[
        'fuzzyroutines',
    ],

    setup_requires=[
    ],

    tests_require=[
        'pytest',
    ],

    install_requires=[
    ],

    package_data={
        '': [
            './fuzzyroutines/*'
            './tests/*'

            'LICENSE',
            'README.md',
        ],
    },

    zip_safe=True,
)
