__author__ = 'olya-livchak'

import matplotlib.pyplot as plt
import math
import numpy


N = int()
N = 6


def bernulli(N):
    p = 1/(N+1)
    q = 1 - p
    f = []
    arg_x = []
    for x in range(0, 2):
        if (x == 0) or (x == 1):
            res = ((p**x)*(q**(x-1)))
            f.append(res)
            arg_x.append(x)
        else:
            f.append(0)
            arg_x.append(x)
    plt.figure(1)
    plt.plot(arg_x, f)
    plt.title("Бернуллі")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    return x, p
bernulli(N)


def factorial(i):
    if i == 0:
        return 1
    return i*factorial(i - 1)
print(factorial(0))


def komb(n, k):
    return factorial(n)/((factorial(k)) * (factorial(n-k)))
print(komb(1, 1))


def binominalny(N):
    n = (N + 20)
    p = float(1/(N+1))
    q = float(1-p)
    f = []
    x_ax = []
    for x in range(0, n+1):
        #if x <= 1:
        res = (komb(n, x)*((pow(p, x))*(pow(q, (1-x)))))
        f.append(res)
        x_ax.append(x)
    plt.plot(x_ax, f)
    plt.title("Біномінальний розподіл")
    plt.show()
    return x, p
binominalny(N)


def puasson(N):
    l = N + 20
   # e = float(2.7)
    n = int(N + 20)
    res = float()
    f = []
    arg_x = []
    for x in range(0, 50):
            res = (pow(l, x) / factorial(x)) * math.exp(-l)
            f.append(res)
            arg_x.append(x)
    plt.plot(arg_x, f)
    plt.title("Пуассон")
    plt.show()
    return x, l
puasson(N)


def rivn(N):
    a = -N
    b = N
    arg_x = []
    f = []
    for x in range(a, b):
        if(x > a) or (x < b):
            res = 1/(b-a)
            f.append(res)
            arg_x.append(x)
        else:
            f.append(0)
            arg_x.append(x)
    plt.plot(arg_x, f)
    plt.title("Рівномірний р-л")
    #plt.legend("R")
    plt.show()
    return x, b
rivn(N)


def norm(N):
    a = N
    d = N/2
    f = []
    arg_x = []
    for x in range(-35, 35):
        res = (1/(d*math.sqrt(2 * (math.pi))) * (math.exp(-(pow(x-a, 2))/(2*(d**2)))))
        f.append(res)
        arg_x.append(x)
    plt.plot(arg_x, f)
    plt.title("Нормальний р-л")
    #plt.legend("N")
    plt.show()
    return a, d
norm(N)


def pareto(N):
    l = 3
    f = []
    res = float()
    arg_x = []
    x0 = 1
    for x in range(100, 600):
        if x/100 >= x0:
            res = (l*pow(x0, l))/(pow(x/100, l+1))
            f.append(res)
            arg_x.append(x/100)
        else:
            f.append(0)
            arg_x.append(x)
            print(x,res)
    plt.plot(arg_x, f)
    plt.title("Парето")
    plt.show()
    return x0, l
pareto(N)


def gamma(n, diff):
    minus = n-diff
    if minus == 0:
        return 1
    if minus == 1:
        return 1
    return (minus) * gamma(minus-2, 0)


def student(N):
    l = N
    arg_x = []
    f = []
    for x in range(-300, 300):
        res = (gamma(l, 1)/(math.pi*pow(l, 0.5)*gamma(l, 2)))*math.pow(((1+(x * x/1000)/l)), ((-l+1)/2))
        f.append(res)
        arg_x.append(x/100)
    plt.plot(arg_x, f)
    plt.title("Ст’юдента")
    #plt.legend("P")
    plt.show()
    return x, l
student(N)


def maxvell_bolcman(N):
    arg_x = []
    f = []
    a = N
    for x in range(0, 100):
        part1 = math.sqrt(2/math.pi)
        part2 = x**2*math.exp((-x**2/(2*a**2)))
        part3 = math.pow(a, 3)
        res = (part1 * part2)/part3
        f.append(res)
        arg_x.append(x)
    plt.plot(arg_x, f)
    plt.title("Максвела-Больцмана")
    plt.show()
    return x, a
maxvell_bolcman(N)


def fermi_diraka(N):
    arg_x = []
    f = []
    m = 1.69
    #t = 290
    #k = m/10 #0.0138 #1.38*math.pow(10, -23)
    for x in range(-30, 30):
        part1 = math.exp((x/10-m)/(m/10))
        res = 1/(part1 + 1)
        f.append(res)
        arg_x.append(x/10)
    plt.plot(arg_x, f)
    plt.title("Фермі - Дірака")
    plt.show()
    return x, m
fermi_diraka(N)


def lorenc(N):
    f = []
    arg_x = []
    y = 0.5
    x0 = 0
    for x in range(-50, 50):
        part1 = 1/math.pi
        part2 = y/((math.pow(x/10-x0, 2))+(math.pow(y, 2)))
        res = part1*part2
        f.append(res)
        arg_x.append(x/10)
        plt.plot(arg_x, f)
    plt.title("Розподіл Коші-Лоренца")
    plt.show()
    return x, y
lorenc(N)


def voigt(N):
    f = []
    arg_x = []
    a = 1
    x_c = 5
    y0 = 0
    wg = 1
    wl = 1
    for x in range(1, 1000):
        f1_p1 = (2*a)/math.pi
        f1_p2 = wl/((4*(math.pow(x/100-x_c, 2))) + math.pow(wl, 2))
        f1 = f1_p1*f1_p2
        f2_p1 = math.sqrt((4*math.log2(x))/math.pi)
        f2_p2 = math.exp(((-4*math.log2(x))/(wg**2))*(x/100**2))/wg
        f2 = f2_p1*f2_p2
        res = y0+(f1*f2)*x/100
        f.append(res)
        arg_x.append(x/100)
        plt.plot(arg_x, f)
    plt.title("Розподіл Фогта")
    plt.show()
    return x, x_c
voigt(N)