"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
from typewriter import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='typewriter',
    version=__version__,
    description='A simple Python module that allows you to print out strings using a "typewriter" like effect.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/FujiMakoto/python-typewriter',

    # Author details
    author='Makoto Fujimoto',
    author_email='makoto@makoto.io',

    # License
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords=['typewriter', 'typewrite', 'typewriting', 'print animation', 'text animation', 'console animation'],

    py_modules=['typewriter']
)