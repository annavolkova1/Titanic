import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')


def get_number_of_pass_from_port(port, data = None):
    """
        Подсчитайте сколько пассажиров загрузилось на борт в различных портах?
        Приведите три числа через пробел.
    """
    ports = data.value_counts()

    if port == 'S':
        return ports['S']
    else:
        if port == 'C':
            return ports['C']
        else:
            return ports['Q']


Q = get_number_of_pass_from_port('Q', data['Embarked'])
C = get_number_of_pass_from_port('C', data['Embarked'])
S = get_number_of_pass_from_port('S', data['Embarked'])


print(Q, C, S)
