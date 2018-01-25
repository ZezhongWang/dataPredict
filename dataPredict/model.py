# -*- coding: utf-8 -*-
__author__ = 'w2w'
__date__ = '18-1-25 上午11:41'
from sklearn import linear_model
from sklearn import svm


class LearningModel(object):
    def __init__(self, method='LinearRegression'):
        self._method = method
        if method == 'LinearRegression':
            self.reg = linear_model.LinearRegression()
        if method == 'svm':
            self.reg = svm.SVR(C=0.1)

    def fit(self, train_data, train_label):
        self.reg.fit(train_data, train_label)

    def predict(self, test_data):
        pred_label = self.reg.predict(test_data)
        return pred_label

    def score(self, train_data, test_label):
        score = self.reg.score(train_data, test_label)
        return score

    def MSE(self, test_label, pred_label):
        length = len(test_label)
        mse = 0
        for index in range(length):
            mse += (test_label[index]-pred_label[index])**2
        return mse