# Заполните массив длины N случайными числами в интервале [0,5].
# Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 7
# [1, 2, 3, 3, 2, 2, 1]
# Вывод:
# значение:3 индексы 2 и 3
# значение:2 индексы 4 и 5

import random
g = []
i = 0
conter1 = 0
m = None
stop = int(input('введите количество эллементов в списке'))
while True:
    if i == stop:
        break
    t = random.randint(0,5)
    g.append(t)
    i = i+1
for r in g:
    conter1 = conter1 + 1
    conter2 = 0
    for j in g:
        conter2 = conter2 + 1
        if r == j and (conter2 - 1 == conter1):
            print(conter1, conter2)
print(g)