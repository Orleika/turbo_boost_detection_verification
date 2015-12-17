#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import numpy as np
import time
from datetime import datetime
import httpagentparser

def main():
    client = MongoClient()
    db = client.turbo

    t = []
    for data in db.lancers.find():
        if data['4thUpdate'] != '' and httpagentparser.detect(data['http_User-Agent'])['browser']['name'] == 'Microsoft Internet Explorer':
            t1 = time.mktime(time.strptime(data['4thUpdate'], '%Y-%m-%d %H:%M:%S'))
            t2 = time.mktime(time.strptime(data['5thUpdate'], '%Y-%m-%d %H:%M:%S'))
            t.append(t2 - t1)

    result = np.array(t)
    print t
    print "ave %0.2f (+/- %0.2f)" % (np.average(result), np.std(result))
    print np.max(result)

if __name__ == '__main__':
    main()
