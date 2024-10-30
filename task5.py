# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.

t = (input())
t=list(map(int, t.split()))
print(t)
x =0
print(len(t))
m=0
for i in t:
    if i > m:
        m = i
        count = 0
    elif m == i:
        count = count+1
print(count+1)
# print(m)
# for i in t:
#     if i == m:
#         x = x + 1
# print(x)
