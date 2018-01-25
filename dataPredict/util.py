# -*- coding: utf-8 -*-
__author__ = 'w2w'
__date__ = '18-1-25 上午10:40'

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

def get_file_list(file_dir):
    # acquire all complete .csv file path under a file director
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for f in files:
            if os.path.splitext(f)[1] == '.csv':
                file_list.append(os.path.join(root, f))
    return file_list


def load_data(file_path):
    # read the .csv file
    data = pd.read_csv(file_path)
    return data


def load_all_data(file_list):
    # load all .csv file
    # return a dict with key is code, and data is DataFrame
    stocks_data_dict = {}
    for f in file_list:
        stock_data = load_data(f)
        code = get_code(f)
        stocks_data_dict[code] = stock_data
    return stocks_data_dict


def get_code(file_path):
    # get the stock code string in a file path
    dir_length = file_path.rfind('/')
    post_fix_length = 4
    code = file_path[dir_length+1:-post_fix_length]
    return code


def dropNa(X, y):
    data = pd.concat([X, y], axis=1)
    data = data.dropna(axis=0, how='any')
    columns = data.columns
    X = data[columns[:-1]]
    y = data[columns[-1]]
    return X, y


def draw_p_change_line_chart(code, y_true, y_pred):
    sns.set()
    length = len(y_true)
    test_length = len(y_pred)
    plt.figure(1)
    plt.plot(range(length), y_true, 'o-', label='p_change_true')
    plt.plot(range(length - test_length, length), y_pred, 'o:', label='p_change_predict')
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('p_change')
    plt.title("Complete Stock " + code + " p_change line chart")
    file_name = code + '.png'
    plt.savefig(os.path.join('picture', file_name))
    plt.figure(2)
    plt.plot(range(length - test_length, length), y_true[-test_length:], 'o-', label='p_change_true')
    plt.plot(range(length - test_length, length), y_pred, 'o:', label='p_change_predict')
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('p_change')
    plt.title("Part Stock " + code + " p_change line chart")
    pfile_name = code + 'p.png'
    plt.savefig(os.path.join('picture', pfile_name))


def normalize(X):
    norm = preprocessing.Normalizer()
    X = norm.fit_transform(X)
    return pd.DataFrame(X)


def minMaxScalar(X):
    scalar = preprocessing.MinMaxScaler()
    X = scalar.fit_transform(X)
    return pd.DataFrame(X)
