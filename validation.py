#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def main():
    bench = np.loadtxt('./data/training_ie_merge.txt', delimiter = '\t')
    data_train = [[x[1]] for x in bench]
    label_train = [int(x[0]) for x in bench]
    estimator = LinearSVC()
    estimator.fit(data_train, label_train)
    label_predict = estimator.predict(data_train)

    print accuracy_score(label_train, label_predict)
    target_names = ['TB off', 'TB on']
    print(classification_report(label_train, label_predict, target_names=target_names))

if __name__ == '__main__':
    main()
