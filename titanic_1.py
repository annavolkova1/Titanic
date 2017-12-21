import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')


def percentage(perc, whole):
    return (perc * 100) / whole


def get_number_of_pass(sex, data = None):
    """
        Какое количество мужчин и женщин ехало на параходе?
        Приведите два числа через пробел
    """
    sexratio = data.value_counts()

    if sex == 'male':
        return sexratio['male']
    else:
        return sexratio['female']


male_int = get_number_of_pass('male', data['Sex'])
female_int = get_number_of_pass('female', data['Sex'])


total_int = male_int + female_int
print(round(percentage(male_int, total_int)), round(percentage(female_int, total_int)))
