# -*- coding: utf-8 -*-
__author__ = 'w2w'
__date__ = '18-1-25 上午11:35'
from fastResearchData import FastResearchData
from indicatorGallexy import IndicatorGallexy
from util import *
import argparse
from modelEngine import ModelEngine
import warnings


if __name__ == '__main__':
    warnings.filterwarnings("ignore")

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="the directory of the .csv file")
    parser.add_argument("code", type=int, help="the stock code you want to predict")
    parser.add_argument("-m", "--method", type=str,
                        default='LinearRegression', help="the method used to do this task")
    parser.add_argument("-r", "--ratio", type=float,
                        default=0.1, help="the validate data set ratio")
    # parser.add_argument("-p", "--preprocess", help="preprocessing or not", action='store_true')
    parser.add_argument("-a", "--ahead", help="the number of p_change look ahead",
                        default=0.1, action='store_true')
    args = parser.parse_args()

    file_path = args.filepath
    code = str(args.code)
    method = args.method

    frData = FastResearchData(file_path)

    # dataDF = getDataFromDB("DBPATH")
    frData.loadStockData(code)
    # DataFrame并不一定很快，但是很多数据最开始的格式很可能是DataFrame，
    # 所以可以用这一步进行预处理，转换为我们内部一个更快格式的数据
    # frData.loadFromDataFrame()
    frData.dumpToHDF5()
    # 这里存放了我们的一堆指标计算方法
    # 我们可以将各种指标分成不同的类，以此来管理各种各样的不同分类指标
    xmIG = IndicatorGallexy(frData)
    # rIG = NewTypeOfIndicatorGallexy()

    # y = xmIG.getNext(frData, 'priceChange')
    # x1 = xmIG.getAvgPrc(frData, 'open')
    # x2 = xmIG.getMACD(frData, 'close', 1, 1)
    # x3 = rIG.getNewIND(frData, 'pp')
    X1 = xmIG.getAheadData(code, 'p_change', interval=10)
    X2 = xmIG.getAvgPrc(code, 'open', interval=10)
    # X3 = xmIG.getAheadMax(code, 'volume', interval=10)
    y = xmIG.getPChange(code, 'p_change')
    # ModelEngine是一个管理训练和评估过程的类
    # 可以在ModelEngine中选择不同的模型，以及不同的训练方法，以及不同的变量
    X = pd.concat([X1, X2], axis=1)

    # drop Nan
    X, y = dropNa(X, y)

    me = ModelEngine(method)
    me.addXs(X)
    me.setY(y)
    me.train()
    y_predict = me.predict()
    draw_p_change_line_chart(code, y_true=y, y_pred=y_predict)
    # 最终可以用Outsample的结果去验证我们模型的好坏
    train_loss, test_loss = me.evaluateOutSample()
    print 'Train Loss = ' + str(train_loss)
    print 'Test Loss = ' + str(test_loss)
    print 'Predict result = ' + str(y_predict)
