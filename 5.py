__author__ = 'olya-livchak'

import matplotlib.pyplot as plt
import  random
from collections import Counter
import math


def herz(random_array=[], output=str()):
    random_array = sorted(random_array)
    counter = 0
    herz_value = []
    herz_x = []
    ser = float()
    moda = float()
    med = float()
    logaryfm = float()
    geom = float()
    seredn_kv = float()
    seredn_garm = float()
    garm_znam = float()
    log_counter = 0
    for i in range(0, len(random_array)):
        if random_array[i] != 0:
            logaryfm += math.log(random_array[i])
            garm_znam += 1/(random_array[i])
            log_counter += 1

        if random_array[i+1] == random_array[len(random_array)-1]:
            herz_value.append(counter)
            herz_x.append(random_array[i])
            if output == "x":
                return herz_x
            if output == "y":
                return herz_value
            if output == "serednye":
                return ser/3000
            break
        if random_array[i] == random_array[i+1]:
            counter += 1
            continue
        if random_array[i] != random_array[i+1]:
            herz_value.append(counter)
            herz_x.append(random_array[i])
            counter = 0
            continue
    ser += random_array[i]
    geom = math.exp(logaryfm/log_counter)
    seredn_garm = math.sqrt(log_counter/garm_znam)
    med = len(random_array)/2
    if len(random_array) % 2 == 0:
        med = (random_array[int(len(random_array)/2)] + random_array[int(len(random_array)/2-1)])/2

    seredn_kv = math.sqrt((1/N)*math.pow(random_array[i], 2))
    print('Мода = ', Counter(random_array).most_common(1))
    print('Середнє = ', ser)
    print('Медіана = ', med)
    print('Середнє геометричне = ', geom)
    print('Середнє квадратичне = ', seredn_kv)
    print('Середнє гармонічне = ', seredn_garm)


N = 6
rand_array = []


for i in range(0, 3000):
    r = random.randint(0, 10*N)
    rand_array.append(r)
print(herz(rand_array))
plt.plot(herz(rand_array, "x"), herz(rand_array, "y"))
plt.title('Задана послідовність випадкових чисел')
plt.show()