#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import numpy as np
import httpagentparser

def get_std(tb):
    dict = {"Typescript": [], "Richards": [], "DeltaBlue": [], "Crypto": [], "RayTrace": [], "EarleyBoyer": [], "RegExp": [], "Splay": [], "SplayLatency": [], "NavierStokes": [], "PdfJS": [], "Mandreel": [], "MandreelLatency": [], "Gameboy": [], "CodeLoad": [], "Box2D": [], "zlib": []}
    client = MongoClient()
    db = client.turbo
    result = []
    for data in db.statics4.find({'tb': tb}):
        if httpagentparser.detect(data['useragent'])['browser']['name'] == 'Chrome':
            for score in data['scores']:
                dict[score['name']].append(int(score['score']))
    result = []
    for key, value in dict.iteritems():
        result.append(key + '\t' + '\t'.join(map(str, value)) + '\n')
    f = open('./statics.txt', 'w')
    f.writelines(result)
    f.close()

        # std[key] = np.std(np.array(value))
        # ave[key] = np.average(np.array(value))
    # for key, value in sorted(std.items(), key = lambda x:x[1]):
    #     print key, value

def main():
    get_std(True)

if __name__ == '__main__':
    main()
