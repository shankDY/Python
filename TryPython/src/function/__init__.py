# # правильное описание функции
# def add(a, b):
#     return a + b
#
#
# if __name__ == '__main__':
#     add(1, 2)
#     v = add(1, 5)

# ошибка( функция должна быть объявлена выше функции main, т.е до первого вызова функции)
# def add(a, b):
#     return a + b


# def f(n):
#     return n * 10 + 5
#
#
# if __name__ == '__main__':
#
#     i = f(f(f(10)))
#     print(i)

# # функция поиска минимума, которая принимает любое количество аргументов
# def min(*a):
#     m = a[0]
#     for x in a:
#         if m > x:
#             m = x
#     return m
#
#
# if __name__ == '__main__':
#     print(min(5))
#     print(min(5, 3))
#     print(min(5, 3, 6, 7, 8, 9, 1, -1))
#
#     # вернет нам список целеком, т.к * загонит список в кортеж, и этот список будет являться его первым элементом
#     print(min([5, 3, 6, 7, 8, 9, 1, -1]))


# # данная функция принимает два обязательных параметра и один необязательный. тут задано значение по умолчанию
# def my_range(start, stop, step=1):
#     res = []
#     if step > 0:
#         x = start
#         while x < stop:
#             res += [x]
#             x += step
#     elif step < 0:
#         x = start
#         while x > stop:
#             res += [x]
#             x += step
#     return res
#
#
# if __name__ == '__main__':
#     print(my_range(2, 5))
#     print(my_range(2, 15, 3))
#     print(my_range(15, 2, -3))


"""

Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

f(x)=⎧⎩⎨⎪⎪1−(x+2)2,−x2,(x−2)2+1,при x≤−2при −2<x≤2при 2<x



def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -(x / 2)
    return ((x-2)**2)+1


if __name__ == '__main__':
    x = int(input())
    print(f(x))
"""

"""

Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, 
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, 
например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации.

"""


# класический способ создания списка
# def modify_list(l):
#     v = []
#     for item in l:
#         if not item % 2:
#             item = item // 2
#             v.append(item)
#     l.clear()
#     l.extend(v)
#     return l

# # тоже самое , но с помощью генератора списков
def modify_list(l):
    """
    логика такая, так как список l в памяти уже есть и его нужно перезаписать, то есть изменить сам объект списка,
    поэтому тут я делаю срез всего списка от начала до конца и меняю сам объект.
    если написать просто l = [i//2 for i in l if not i % 2] в данном случае будет создан новый объект,
    под него выделена память и переменная l будет уже ссылаться на него, а старая ссылка на
    исходный объект списка сотрется. т.е происходит не изменение объекта, а перенаправление ссылки у переменной l.
 """
    l[:] = [i // 2 for i in l if i % 2 == 0]


if __name__ == '__main__':
    lst = [2, 3, 5, 6]
    modify_list(lst)
    print(lst)
