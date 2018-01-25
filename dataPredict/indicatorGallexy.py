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

    def getAvgPChange(self, columnsName):
        # 行数与之前不一样


        return series

    def getAheadData(self, code, columnName, interval=10):
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
                label = float(row[columnName])
                features.append(label)
                data_set.append(features)
                continue
            row_ahead = origin_df.iloc[index + interval]
            day_ahead = row_ahead[day_column]
            # ensure that the ahead data is in the same day
            # but we don't guarantee that the features and label
            # are in the same afternoon or morning
            if day_ahead == day:
                features = list(origin_df[index + 1:interval + index + 1][columnName])
                features.append(row[time_column])
                label = float(row[columnName])
                features.append(label)
                data_set.append(features)
            # if not in the same day, complete with zeros
            else:
                features = [np.nan]*interval
                features.append(row[time_column])
                label = float(row[columnName])
                features.append(label)
                data_set.append(features)

        data_set = pd.DataFrame(data_set)
        time_col = data_set.columns[-2]
        le = preprocessing.LabelEncoder()
        data_set[time_col] = le.fit_transform(data_set[time_col])
        min_max_scaler = preprocessing.MinMaxScaler()
        data_set[time_col] = min_max_scaler.fit_transform(data_set[time_col])
        return data_set



    def getAvgPrc(self, columnsName="Price",  interval=10):
        pass

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
    print ahead_pchange
