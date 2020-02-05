#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 00:04:46 2020

@author: gdubs
"""

import pandas as pd
import numpy as np


def parse_file():
    df = pd.read_excel(r"/media/gdubs/Extension1/Projects/xsl_checker/files/data1.xlsx")
    print(df)
    
    for i, row in df.iterrows():
        #print(row)
        #a = np.array(row.fillna(''))
        #if(has_duplicates(a)):
        if(is_duplicate(row['valcheck1'], row['valcheck2'])):
            print('duplicate on row ' + str(i))
        else:
            print('no dup')
    
    
def has_duplicates(x):
    return len(np.unique(x)) != len(x)

def is_duplicate(val1, val2):
    return val1 == val2

if __name__ == '__main__':
    pd.set_option('display.max_rows', 10000)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 500)
    parse_file()