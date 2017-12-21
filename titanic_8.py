import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')


"""
    Посчитайте среднюю цену за билет и медиану.
"""

print('Средняя цена за билет')
print(data['Fare'].mean())

print('Цена за билет: медиана')
print(data['Fare'].median())
print()



