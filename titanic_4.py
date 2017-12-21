import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')


def percentage(perc, whole):
    return (perc * 100) / whole


def get_number_of_pass_class(Pclass, data = None):
    """
        Какие доли составляли пассажиры первого, второго, третьего класса?
    """
    pclass = data.value_counts()

    if Pclass == 1:
        return pclass[1]
    else:
        if Pclass == 2:
            return pclass[2]
        else:
            return pclass[3]


A = get_number_of_pass_class(3, data['Pclass'])
B = get_number_of_pass_class(2, data['Pclass'])
C = get_number_of_pass_class(1, data['Pclass'])


total_int = A + B + C
print(round(percentage(A, total_int)), round(percentage(B, total_int)), round(percentage(C, total_int)))

