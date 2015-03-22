try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'geocodertools',
    'version': '0.1.0',
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
    'long_description': ("A tookit geo information"),
    'install_requires': [
        "argparse",
        "nose"
    ],
    'keywords': ['geocoder', 'longitude', 'latitude'],
    'download_url': 'https://github.com/MartinThoma/geocodertools',
    'classifiers': ['Development Status :: 3 - Alpha',
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
