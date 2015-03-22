#!/usr/bin/env python

"""Functions to work with Geo coordinates, reverse geo coding and getting city
   names out of coordinates without internet.
"""

import math
import os
from os.path import expanduser

import logging
import sys

try:
    from urllib.request import urlretrieve
except:
    from urllib import urlretrieve
import zipfile
import msgpack
import geocodertools

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


def download():
    """Download cities database."""
    url = "http://download.geonames.org/export/dump/cities1000.zip"
    logging.info("Download cities from %s", url)

    home = expanduser("~")
    misc_path = os.path.join(home, "geocodertools")
    if not os.path.exists(misc_path):
        os.makedirs(misc_path)
    zip_path = os.path.join(misc_path, "cities1000.zip")
    urlretrieve(url, zip_path)
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(misc_path)


def build_db():
    """Get a structured dataset out of
       http://download.geonames.org/export/dump/cities1000.txt

       TODO: Download it automatically if it is not here.
    """
    home = expanduser("~")
    misc_path = os.path.join(home, "geocodertools")
    if not os.path.exists(misc_path):
        os.makedirs(misc_path)
    cities_path = os.path.join(misc_path, "cities1000.txt")
    cities_msgpack = os.path.join(misc_path, "cities1000.bin")
    if not os.path.isfile(cities_path):
        download()
    if not os.path.isfile(cities_msgpack):
        with open(cities_path) as f:
            lines = f.readlines()

        db = []
        for line in lines:
            l = line.strip().split('\t')
            db.append({'geonameid': int(l[0]),
                       'name': l[1],
                       'asciiname': l[2],
                       'alternatenames': l[3],
                       'latitude': float(l[4]),
                       'longitude': float(l[5]),
                       'feature class': l[6],
                       'feature code': l[7],
                       'country code': l[8],
                       'cc2': l[9],
                       'admin1 code': l[10],
                       'admin2 code': l[11],
                       'admin3 code': l[12],
                       'admin4 code': l[13],
                       'population': int(l[14]),
                       'elevation': l[15],
                       'dem': l[16],
                       'timezone': l[17],
                       # datetime.datetime.strptime(l[18], "%Y-%m-%d")
                       'modification date': l[18],
                       'dimensions': get_cartesian(float(l[4]), float(l[5]))})
        packed = msgpack.packb(db, use_bin_type=True)
        with open(cities_msgpack, 'wb') as f:
            f.write(packed)
    else:
        with open(cities_msgpack, 'rb') as f:
            content = f.read()
        db = msgpack.unpackb(content)
    return db


def get_cartesian(lat, lon):
    """
    the x-axis goes through long,lat (0,0), so longitude 0 meets the equator;
    the y-axis goes through (0,90);
    and the z-axis goes through the poles.

    In other words:
    * (0, 0, 0) is the center of earth
    * (0, 0, R) is the north pole
    * (0, 0, -R) is the south pole
    * (R, 0, 0) is somewhere in africa?

    :param lat: latitude in radians
    :param lon: longitude in radians
    """
    R = 6371000.0  # metres
    x = R * math.cos(lat) * math.cos(lon)
    y = R * math.cos(lat) * math.sin(lon)
    z = R * math.sin(lat)
    return [x, y, z]


def find_closest(db, pos):
    """Find the closest point in db to pos."""
    def get_dist(d1, d2):
        lat1, lon1 = d1['latitude'], d1['longitude']
        lat2, lon2 = d2['latitude'], d2['longitude']
        R = 6371000.0  # metres
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2-lat1)
        delta_delta = math.radians(lon2-lon1)

        a = math.sin(delta_phi/2) * math.sin(delta_phi/2) + \
            math.cos(phi1) * math.cos(phi2) * \
            math.sin(delta_delta/2) * math.sin(delta_delta/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        d = R * c
        return d
    closest_dataset, closest_dist = db[0], get_dist(pos, db[0])
    for dataset in db:
        dist = get_dist(pos, dataset)
        if dist < closest_dist:
            closest_dataset = dataset
            closest_dist = dist
    return closest_dataset


class geoquery(object):
    """TODO: NOT READY.

    Datastructure for nearest neighbor searches.
    """
    def __init__(self, db):
        # Each element in this list has to be a dictionary with 'min', 'max'
        self.dimensions = []

        if len(db) > 1000:
            d = []
            for i in range(1, 5):
                d.append([])
                while len(d[i]) < len(db) / 5.0:
                    d[i].append()  # TODO

    def get(self, latitude, longitude):
        """Get the closest dataset."""
        pass


class bin(object):
    """Datastructure which simply bins by latitude for nearest neighbor
       searches.
    """
    def __init__(self, db):
        self.bins = {}

        for dataset in db:
            latitude = int(round(dataset['latitude']))
            if latitude in self.bins:
                self.bins[latitude].append(dataset)
            else:
                self.bins[latitude] = [dataset]

    def get(self, pos):
        """Get the closest dataset."""
        latitude = int(round(pos['latitude']))
        return find_closest(self.bins[latitude], pos)


def get_parser():
    """Return the parser object for this script."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("--lat",
                        dest="latitude",
                        required=True,
                        help="Latitude (in -180, 180)")
    parser.add_argument("--lng",
                        dest="longitude",
                        required=True,
                        help="Longitude (in -180, 180)")
    parser.add_argument('--version',
                        action='version',
                        version=('geocodertools %s' % str(geocodertools.__version__)))
    return parser


def get_city(pos, bobj=None):
    if bobj is None:
        db = build_db()
        bobj = bin(db)
    city = bobj.get(pos)
    return city


def main(pos, bobj=None):
    """
    :param pos: A dictionary with {'latitude': 8.12, 'longitude': 42.6}
    :param bobj: An object which has a 'get' method and returns a dictionary.
    """
    city = get_city(pos, bobj)
    for key, value in sorted(city.items()):
        print("%s: %s" % (key, value))


if __name__ == '__main__':
    pos = {'longitude': 8.4229068, 'latitude': 49.0151657}
    pos = {'longitude': -71.312796, 'latitude': 41.49008}
    db = build_db()
    bobj = bin(db)

    import timeit
    a = timeit.timeit('main(pos, bobj)',
                      'from __main__ import main, pos, bobj',
                      number=10)
    print("Nearest City: %s" % bobj.get(pos)['name'])
