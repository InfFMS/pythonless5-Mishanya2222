# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3

import random
g = []
k = 0
i=0
counter1 = 0
m = []
stop = int(input('введите количество эллементов в списке'))
while True :
    i=i+1
    t = random.randint(0,100)
    g.append(t)
    if i == stop:
        break
print(g)
def funk(k):
    if k == stop-1:
        return
    n = []
    count=0
    for j in g:
        count = count + 1
        if g[k] == j:
            n.append(count)
    g.remove(g[k])
    print( 'номера элементов:',n, j)
    k = k + 1
    funk(k)
funk(k)

