import random

N = 6
Q1 = []
Q2 = []
Q3 = []
Q4 = []
Q5 = []
QZ = []


def table_print(table = list()):
    for i in range(0, len(table)):
        if i == len(table)-2:
            print("min", table[i])
        else:
            print(i+1, table[i])
result = list()

for i in range(0, N+3):
    q1 = random.randint(1, 9)
    Q1.append(q1)
    q2 = random.randint(1, 9)
    Q2.append(q2)
    q3 = random.randint(1, 9)
    Q3.append(q3)
    q4 = random.randint(1, 9)
    Q4.append(q4)
    q5 = random.randint(1, 9)
    Q5.append(q5)
    q_z = random.randint(1, 9)
    QZ.append(q_z)
print('Таблиця альтернатив та оцінок: ')
print("Q1: ", Q1)
print("Q2: ", Q2)
print("Q3: ", Q3)
print("Q4: ", Q4)
print("Q5: ", Q5)


def maksimin():
    min_array = list()
    for i in range(0, N+3):
        result1.append([])
        result2.append([])
        result3.append([])
        result4.append([])
        result5.append([])
        #for j in range(0, 9):
        #alt = random.randint(1, 9)
        maks1 = Q1[i]/QZ[i]
        maks2 = Q2[i]/QZ[i]
        maks3 = Q3[i]/QZ[i]
        maks4 = Q4[i]/QZ[i]
        maks5 = Q5[i]/QZ[i]
        result[i].append(round(maks1, 2))
        result[i].append(round(maks2, 2))
        result[i].append(round(maks3, 2))
        result[i].append(round(maks4, 2))
        result[i].append(round(maks5, 2))
    column = list()
    for i in range(0, 9):
        for j in range(0, 9):
            column.append(result[i])
        min_array.append(min(column))
        column = list()
    result.append(min_array)
    result.append(max(min_array))

    return result
result = maksimin()
table_print(result)