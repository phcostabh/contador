#!/usr/bin/python

import sys
import operator
import itertools
import simplejson

import redis

_client = redis.Redis()


def get_category_data(keys):
    data = ((long(k.split(':')[2]), _client.scard(k)) for k in keys)
    return sorted(data, key=operator.itemgetter(1), reverse=True)


def get_top(category=None):
    pattern = 'v:*' if category is None else 'v:%s:*' % (category)
    keys = _client.keys(pattern)
    by_category = itertools.groupby(keys, key=lambda k: k.split(':')[1])
    return dict((c, get_category_data(ks)) for c, ks in by_category)


def main():
    category = None if len(sys.argv) == 1 else sys.argv[1]
    data = get_top(category)
    simplejson.dump(data, sys.stdout)


if __name__ == '__main__':
    main()
