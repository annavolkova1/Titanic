import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')


"""
    Посчитайте средний возраст пассажиров и медиану.
"""

print('Средний возраст пассажиров')
print(data['Age'].mean())

print('Возраст пассажиров: медиана')
print(data['Age'].median())
print()



