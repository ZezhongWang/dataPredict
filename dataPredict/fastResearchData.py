# -*- coding: utf-8 -*-
__author__ = 'w2w'
__date__ = '18-1-25 上午10:38'
import pandas as pd
import os
from util import get_code


class FastResearchData:
    def __init__(self, dir_path):
        self.stock_dict = {}
        self.dir_path = dir_path

    def loadFromDataFrame(self, stock_code, df):
        if stock_code not in self.stock_dict.keys():
            self.stock_dict[stock_code] = df
        else:
            pd.concat([self.stock_dict[stock_code], df], axis=0)

    def loadStockData(self, stock_code):
        df = pd.read_csv(os.path.join(self.dir_path, stock_code+'.csv'))
        if stock_code not in self.stock_dict.keys():
            self.stock_dict[stock_code] = df
        else:
            pd.concat([self.stock_dict[stock_code], df], axis=0)

    def loadFromCSV(self,path):
        code = get_code(path)
        df = pd.read_csv(path)
        self.loadFromDataFrame(code, df)

    def getDataFrame(self, code):
        return self.stock_dict[code]

    def getStockDict(self):
        return self.stock_dict

    def dumpToHDF5(self):
        store = pd.HDFStore(os.path.join(self.dir_path, 'data.h5'))
        for items in self.stock_dict.items():
            code = items[0]
            df = items[1]
            store.put(code, df)
        store.close()

if __name__ == '__main__':
    path = '/home/w2w/PycharmProjects/dataPredict/data'
    fd = FastResearchData(path)
    code1 = '000022'
    df = pd.read_csv(os.path.join(path, code1+'.csv'))
    fd.loadFromDataFrame(code1, df)
    code2 = '000023'
    df = pd.read_csv(os.path.join(path, code2+'.csv'))
    fd.loadFromDataFrame(code2, df)

    code3 = '000025'
    fd.loadStockData(code3)
    fd.dumpToHDF5()
