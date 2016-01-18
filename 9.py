import random

N = 6
Q1 = []
Q2 = []
Q3 = []
Q4 = []
A = []
maximum = []
index = []

for i in range(0, N+3):
    q1 = random.randint(0, 5)
    Q1.append(q1)
    q2 = random.randint(0, 5)
    Q2.append(q2)
    q3 = random.randint(0, 5)
    Q3.append(q3)
    q4 = random.randint(0, 5)
    Q4.append(q4)
maximum = max(Q1)
index.append(maximum)

print('Таблиця альтернатив та оцінок: ')
print("Q1: ", Q1)
print("Q2: ", Q2)
print("Q3: ", Q3)
print("Q4: ", Q4)
print("Лексикографічне упорядкування:")
for count in enumerate(Q1):
    if count[1] == maximum:
        print('У першому випадку:')
        print("A", count[0]+1)
        break

for count in enumerate(Q4):
    if count[1] == maximum:
        print('У другому випадку:')
        print("A", count[0]+1)
        break
alt = []


def poslidovn(alt):
    maximum_Q1 = []
    maximum_Q2 = []
    maximum_Q3 = []
    value_Q3 = []
    value_Q2 = []
    sum_A1_A2 = int()
    A1 = int()
    n = int()
    for i in range(0, N+3):
        maximum_Q1 = max(Q1)
        maximum_Q2 = max(Q2)
        maximum_Q3 = max(Q3)
        sum_A1_A2 = maximum_Q1 + maximum_Q2
    if maximum_Q1 > maximum_Q2:
        n = maximum_Q1 - maximum_Q2

    else:
        n = maximum_Q2 - maximum_Q1

    if maximum_Q3 < maximum_Q2:
        maximum_Q3_new = maximum_Q2 - n

    if maximum_Q3 > maximum_Q2:
        value_Q3 = maximum_Q3 - n

    else:
        value_Q2 = maximum_Q2

    for count in enumerate(Q2):
        if count[1] == value_Q2:
            print('М-д послідовних поступок:')
            print("A", count[0]+1)
        break

    for count in enumerate(Q3):
        if count[1] == value_Q3:
            print('Метод послідовних поступок:')
            print("A", count[0]+1)
        break
    return maximum_Q2, maximum_Q3
    #print(maximum_Q1, maximum_Q2, A1)
print(poslidovn(alt))
