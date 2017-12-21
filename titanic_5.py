import pandas as pd
import numpy as np


data = pd.read_csv('train.csv', index_col='PassengerId')


"""
    Вычислите коэффициент корреляции Пирсона между
    количеством супругов (SibSp) и количеством детей (Parch).
"""

sibsp_arr = data['SibSp']
parch_arr = data['Parch']


pearson_int = np.corrcoef(sibsp_arr, parch_arr)

ages_lst = data['Age'].value_counts().index.tolist()

print(np.average(ages_lst))


