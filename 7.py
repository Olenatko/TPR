__author__ = 'olenyatko'

import random


def table_print(table=list()):
    for i in range(0, len(table)):
        if i == len(table)-2:
            print("min:", table[i])
        else:
            print('критерії:', i+1, table[i])
result = list()


def maksimin():
    min_array = list()
    print('            альтернативи:')
    for i in range(0, 5):
        result.append([])

        for j in range(0, 9):
            alt = random.randint(1, 9)
            q_z = random.randint(1, 9)
            maks = alt/q_z
            result[i].append(round(maks, 1))
    column = list()
    for i in range(0, 5):
        for j in range(0, 5):
            column.append(result[j][i])
        min_array.append(min(column))
        column = list()
    result.append(min_array)
    result.append(max(min_array))
    return result
result = maksimin()
table_print(result)







