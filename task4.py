# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка

import random

t = [random.randint(0, 100) for i in range(int(input()))]

x  = 0
for i in t:
    x = x + i
sred = x / len(str(t))

for j in t:
    if j<=0.7*sred or j >= 1.3*sred:
        t.remove(j)
print(t)