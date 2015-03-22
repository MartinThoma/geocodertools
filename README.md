[![Build Status](https://travis-ci.org/MartinThoma/geocodertools.svg?branch=master)](https://travis-ci.org/MartinThoma/geocodertools)
[![Coverage Status](https://img.shields.io/coveralls/MartinThoma/geocodertools.svg)](https://coveralls.io/r/MartinThoma/geocodertools?branch=master)
[![Documentation Status](http://img.shields.io/badge/docs-latest-brightgreen.svg)](http://pythonhosted.org/geocodertools)
[![Code Health](https://landscape.io/github/MartinThoma/geocodertools/master/landscape.svg)](https://landscape.io/github/MartinThoma/geocodertools/master)

## Installation

```bash
# pip install geocodertools
$ geocodertools --lng 8.40 --lat 49.3
```

## Usage

### Command line

```bash
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
```

### Python

```python
import geocodertools.reverse as geo
city = geo.get_city({'latitude': 8.2, 'longitude': 49.2})
```