# %load q06_sub_total/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q05_replace_missing_values.build import q05_replace_missing_values

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q06_sub_total(path1,path2):
    'write your solution here'
    df = q05_replace_missing_values(path1,path2)
    #print(df)
    df1 = df.groupby('abbr').sum()
    return df1





