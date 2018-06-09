# core modules
import io
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(os.path.join(os.path.dirname(__file__), file_name),
                 encoding='utf-8') as f:
        return f.read()

config = {
    'name': 'geocodertools',
    'version': '0.1.7',
    'author': 'Martin Thoma',
    'author_email': 'info@martin-thoma.de',
    'maintainer': 'Martin Thoma',
    'maintainer_email': 'info@martin-thoma.de',
    'packages': ['geocodertools'],
    'scripts': ['bin/geocodertools'],
    'package_data': {'geocodertools': ['misc/*']},
    'platforms': ['Linux', 'MacOS X', 'Windows'],
    'url': 'https://github.com/MartinThoma/geocodertools',
    'license': 'MIT',
    'description': ('Functions to work with Geo coordinates, reverse geo '
                    'coding and getting city names out of coordinates without '
                    'internet'),
    'long_description': read('README.md'),
    'long_description_content_type': 'text/markdown',
    'install_requires': [
        "argparse",
        "nose"
    ],
    'keywords': ['geocoder', 'longitude', 'latitude'],
    'download_url': 'https://github.com/MartinThoma/geocodertools',
    'classifiers': ['Development Status :: 7 - Inactive',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'Intended Audience :: Science/Research',
                    'License :: OSI Approved :: MIT License',
                    'Natural Language :: English',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.3',
                    'Programming Language :: Python :: 3.4',
                    'Topic :: Software Development',
                    'Topic :: Utilities'],
    'zip_safe': False,
    'test_suite': 'nose.collector'
}

setup(**config)
