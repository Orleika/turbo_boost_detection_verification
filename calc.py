#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Turbo Boost 推定(Octane スコア)

from pymongo import MongoClient
import httpagentparser

def main():
    client = MongoClient()
    db = client.turbo
    result = []

    for data in db.lancers.find():
        row = '\t'.join([httpagentparser.detect(data['http_User-Agent'])['browser']['name'], str(data['tb']), str(data['model']), str(data['RegExp']), str(data['NavierStokes']), str(data['CodeLoad']), str(data['Mandreel']), str(data['MandreelLatency']), str(data['Crypto']), str(data['PdfJS']), str(data['Typescript']), str(data['Splay']), str(data['zlib']), str(data['EarleyBoyer']), str(data['SplayLatency']),  str(data['Richards']), str(data['Box2D']), str(data['RayTrace']), str(data['Gameboy']), str(data['DeltaBlue'])]) + '\n'
        result.append(row.encode('utf8'))

    f = open('./result.txt', 'w')
    f.writelines(result)
    f.close()

if __name__ == '__main__':
    main()
