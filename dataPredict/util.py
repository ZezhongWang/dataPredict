# -*- coding: utf-8 -*-
__author__ = 'w2w'
__date__ = '18-1-25 上午10:40'

import os
import pandas as pd


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

