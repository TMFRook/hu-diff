# -*- coding: utf-8; mode: python; -*-
from setuptools import setup, find_packages

setup(
    name='hu-diff',
    version='0.0.1',
    description="A package that makes difflib more readable also easier to process.",
    long_description="Replace difflib's pure string implementation.",
    license='BSD',
    keywords='difflib diffs human readable',
    url='https://github.com/scrummyin/hu-diff',
    author='Brian Faherty',
    author_email='anothergenericuser@gmail.com',
    maintainer='Brian Faherty',
    maintainer_email='anothergenericuser@gmail.com',
    packages= find_packages(),
    install_requires = [],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 ],
    )
