# -*- coding: utf-8 -*-
__author__ = 'w2w'
__date__ = '18-1-25 上午10:38'
import numpy as np
import pandas as pd
from util import *
from sklearn import preprocessing
from fastResearchData import FastResearchData

class IndicatorGallexy:
    def __init__(self, frData):
        self._frData = frData

    def getNext(self):
        pass

    def getAheadData(self, code, columnsName, interval=10):
        stock_dict = self._frData.getStockDict()
        origin_df = stock_dict[code]
        data_set = []
        day_column = 'day'
        time_column = 'time'
        for index in range(len(origin_df)):
            row = origin_df.iloc[index]
            day = row[day_column]
            # fill the earliest column
            if index + interval >= len(origin_df):
                features = [np.nan] * interval
                features.append(row[time_column])
                data_set.append(features)
                continue
            row_ahead = origin_df.iloc[index + interval]
            day_ahead = row_ahead[day_column]
            # ensure that the ahead data is in the same day
            # but we don't guarantee that the features and label
            # are in the same afternoon or morning
            if day_ahead == day:
                features = list(origin_df[index + 1:interval + index + 1][columnsName])
                features.append(row[time_column])
                data_set.append(features)
            # if not in the same day, complete with zeros
            else:
                features = [np.nan]*interval
                features.append(row[time_column])
                data_set.append(features)

        data_set = pd.DataFrame(data_set)
        time_col = data_set.columns[-1]
        le = preprocessing.LabelEncoder()
        data_set[time_col] = le.fit_transform(data_set[time_col])
        min_max_scaler = preprocessing.MinMaxScaler()
        data_set[time_col] = min_max_scaler.fit_transform(data_set[time_col])
        return data_set

    def getAheadAverage(self, code, columnsName, interval=10):
        return self.getAheadCalc(np.average, code, columnsName, interval)

    def getAheadMax(self, code, columnsName, interval=10):
        return self.getAheadCalc(np.max, code, columnsName, interval)

    def getAheadMin(self, code, columnsName, interval=10):
        return self.getAheadCalc(np.min, code, columnsName, interval)

    def getAheadCalc(self, function, code, columnsName, interval=10):
        stock_dict = self._frData.getStockDict()
        origin_df = stock_dict[code]
        data_list = []
        day_column = 'day'
        for index in range(len(origin_df)):
            row = origin_df.iloc[index]
            day = row[day_column]
            # fill the earliest column
            if index + interval >= len(origin_df):
                data_list.append(np.nan)
                continue
            row_ahead = origin_df.iloc[index + interval]
            day_ahead = row_ahead[day_column]
            # ensure that the ahead data is in the same day
            # but we don't guarantee that the features and label
            # are in the same afternoon or morning
            if day_ahead == day:
                features = list(origin_df[index + 1:interval + index + 1][columnsName])
                data_list.append(function(features))
            # if not in the same day, complete with zeros
            else:
                data_list.append(np.nan)
        data_list = pd.DataFrame(data_list)
        return data_list

    def getPChange(self, code, columnsName='p_change'):
        return self.getColumn(code, columnsName)

    def getOpen(self, code, columnsName='open'):
        return self.getColumn(code, columnsName)

    def getColumn(self, code, columnName):
        stock_dict = self._frData.getStockDict()
        origin_df = stock_dict[code]
        return pd.DataFrame(origin_df[columnName])

    def getAvgPrc(self, code, columnsName="Price",  interval=10):
        return self.getAheadAverage(code, columnsName, interval)

    def getMACD(self, columnsName,params1, paramse2):
        pass

    def getNewIND(self):
        pass

if __name__ == '__main__':
    path = '/home/w2w/PycharmProjects/dataPredict/data'
    write_path = '/home/w2w/PycharmProjects/dataPredict/'
    fd = FastResearchData(path)
    code1 = '000022'
    df = pd.read_csv(os.path.join(path, code1 + '.csv'))
    fd.loadFromDataFrame(code1, df)
    code2 = '000023'
    df = pd.read_csv(os.path.join(path, code2 + '.csv'))
    fd.loadFromDataFrame(code2, df)

    xmIG = IndicatorGallexy(fd)
    ahead_pchange = xmIG.getAheadData(code1, 'p_change')
    ahead_pchange.to_csv('./a.csv')
    print ahead_pchange
    ahead_avg_open= xmIG.getAvgPrc(code1, 'open')
    print ahead_avg_open
