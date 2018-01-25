# -*- coding: utf-8 -*-
__author__ = 'w2w'
__date__ = '18-1-25 上午10:39'
from model import LearningModel
import pandas as pd


class ModelEngine(object):
    def __init__(self, method='svm', test_set_ratio=0.1):
        self._model = LearningModel(method)
        self._ratio = test_set_ratio
        self.X = pd.DataFrame()
        self.Y = pd.DataFrame()
        self.X_train = pd.DataFrame()
        self.y_train = pd.Series()
        self.X_test = pd.DataFrame()
        self.y_test = pd.Series()

    def setY(self, ySeries):
        self.Y = pd.DataFrame(ySeries)

    def addX(self, name, xSeries):
        self.X[name] = xSeries

    def addXs(self, df):
        self.X = pd.concat([self.X, df], axis=1)

    def delX(self, name):
        del self.X[name]

    def train(self):
        self.train_test_split(self.X, self.Y)
        self._model.fit(self.X_train, self.y_train)

    def predict(self):
        y_predict = self._model.predict(self.X_test)
        return y_predict

    def evaluateOutSample(self):
        return self._model.score(self.X_train, self.y_train), self._model.score(self.X_test, self.y_test)

    def getModel(self):
        return self._model

    def train_test_split(self, X, y):
        num = len(X)
        test_num = int(num * self._ratio)
        self.X_train = X[:-test_num]
        self.y_train = y[:-test_num]
        self.X_test = X[-test_num:].reset_index(drop=True)
        self.y_test = y[-test_num:].reset_index(drop=True)

