import random as rand
import matplotlib.pyplot as plt
import math

N = 6

Q1 = []
Q2 = []
Q_x = []
Alt = []
Perf_Point = []

result_x1 = []
result_x2 = []
for j in range(0, 10):
        x1 = rand.randint(N-3, N+3)
        result_x1.append(x1)
        x2 = rand.randint(N-3, N+3)
        result_x2.append(x2)
print('Координати альтернатив: ')
print("x1:", result_x1)
print("x2:", result_x2)

result_q1 = list()
result_q2 = list()


def alt(q1, q2):
    for j in range(0, 10):
        q1 = ((N/4) * result_x1[j]) + math.pow(result_x2[j], 2)
        result_q1.append(q1)
        q2 = (-2 * math.pow(result_x1[j], 2)) + N * result_x2[j]
        result_q2.append(q2)
    print('Альтернативи:')
    print("Q1:", result_q1)
    print("Q2:", result_q2)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(result_q1, result_q2, 'go')
    counter =0
    for xy in zip(result_q1, result_q2):
        ax.annotate("A"+str(counter), xy=xy, textcoords='offset points')
        counter +=1
    plt.tight_layout()
    plt.xlabel('Q1')
    plt.ylabel('Q2')
    plt.grid()
    plt.show()
    return result_q1, result_q2
alt(Q1, Q2)

result_qx = list()
qx1 = list()
qx2 = list()


def Pareto(q_x):
    max = 0
    max_prev = 0
    for i in range(0, 10):
        if result_q1[i] > max:
            max_prev = max
            max = result_q1[i]
        elif result_q2[i] > max:
            max_prev = max
            max = result_q2[i]
    return max_prev, max
print('Парето-оптимальні:', Pareto(Q_x))


def optym_alt(q_x):
    for i in range(0, 10):
        qx1 = result_q1[i]*0.3
        qx2 = result_q2[i]*0.7
        sum_qx1_qx2 = qx1 + qx2
        result_qx.append(round(sum_qx1_qx2, 2))
    return result_qx
print('Qx:', optym_alt(Alt))

result_point = list()
pf = list()


def Perfect(pf):
    for i in range(0, 10):
        max_q1 = max(result_q1)
        max_q2 = max(result_q2)
        perf = math.sqrt((pow(result_q1[i]-max_q1, 2))+pow(result_q2[i] - max_q2, 2))
        result_point.append(round(perf, 2))
    print('ідеальна точка:', min(result_point))
    return result_point
print('масив ідеальних точок:', Perfect(pf))






