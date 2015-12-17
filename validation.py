#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
from sklearn import svm, grid_search, cross_validation
from sklearn.cross_validation import KFold, StratifiedKFold
from sklearn.metrics import classification_report, accuracy_score

def main():
    bench = np.loadtxt('./data/training_firefox_merge.txt', delimiter = '\t')
    data_train = [[x[1]] for x in bench]
    label_train = [int(x[0]) for x in bench]
    param_grid = {'C':10. ** np.arange(-3,4)}
    svc = svm.SVC(kernel='linear')
    clf = grid_search.GridSearchCV(svc, param_grid = param_grid)
    clf.fit(data_train, label_train)
    loo = cross_validation.LeaveOneOut(len(label_train))
    scores = cross_validation.cross_val_score(svc, data_train, label_train, cv=loo, n_jobs=-1)
    print np.average(np.array(scores))
    print scores

if __name__ == '__main__':
    main()
