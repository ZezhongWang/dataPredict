# -*- coding: utf-8 -*-
__author__ = 'w2w'
__date__ = '18-1-25 上午11:41'
from sklearn import linear_model
from sklearn import svm


class LearningModel(object):
    def __init__(self, method='LinearRegression'):
        if method == 'LinearRegression':
            self.reg = linear_model.LinearRegression()
        elif method == 'svm':
            self.reg = svm.SVR(C=10)
        elif method == 'Bayes':
            self.reg = linear_model.BayesianRidge()
        else:
            print "No this method"
            exit(0)

    def fit(self, X_train, y_train):
        self.reg.fit(X_train, y_train)

    def predict(self, X_test):
        y_predict = self.reg.predict(X_test)
        return y_predict

    def score(self, x_test, y_test):
        """
        The coefficient R^2 is defined as (1 - u/v), where u is the regression
        sum of squares ((y_true - y_pred) ** 2).sum() and v is the residual
        sum of squares ((y_true - y_true.mean()) ** 2).sum().
        :param x_test:
        :param y_test:
        :return: R^2
        """
        score = self.reg.score(x_test, y_test)
        return score
