import pandas as pd
import numpy as np


data = pd.read_csv('train.csv', index_col='PassengerId')


def conv_sex_into_int(data):
    res = []
    for d in data:
        if d == 'male':
            res.append(1)
        else:
            res.append(0)
    return res


"""
    Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
        возрастом и параметром survival;
        полом человека и параметром survival;
        классом, в котором пассажир ехал, и параметром survival.
"""

survived = data['Survived']
age = data['Age'].values.reshape(1, -1)
sex = conv_sex_into_int(data['Sex'])
pclass = data['Pclass']
print("Correl")
print(np.corrcoef(age, survived)[0][1], np.corrcoef(survived, sex)[0][1], np.corrcoef(survived, pclass)[0][1])
