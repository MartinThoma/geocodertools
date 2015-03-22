.. geocodertools documentation master file, created by
   sphinx-quickstart on Sun Mar 22 01:24:19 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

geocodertools's documentation
=============================

Contents:

.. toctree::
   :maxdepth: 2

Installation
------------

.. code:: bash

    # pip install geocodertools
    $ geocodertools --lng 8.40 --lat 49.3

Usage
-----

Command line
~~~~~~~~~~~~

.. code:: bash

    $ geocodertools --lng 8.40 --lat 49.3
    admin1 code: 08
    admin2 code: 00
    admin3 code: 07338
    admin4 code: 07338007
    alternatenames: 
    asciiname: Dudenhofen
    cc2: 
    country code: DE
    dem: 105
    elevation: 
    feature class: P
    feature code: PPLA4
    geonameid: 2934737
    latitude: 49.31861
    longitude: 8.38861
    modification date: 2011-04-25
    name: Dudenhofen
    population: 5709
    timezone: Europe/Berlin

Python
~~~~~~

.. code:: python

    import geocodertools.reverse as geo
    city = geo.get_city({'latitude': 8.2, 'longitude': 49.2})



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

