"""В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для
него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его
вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого n нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное), выводящее это число в
консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с
людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи,
как минимум до 1000 человек. """
a = int(input())
if a % 10 == 1 and a % 100 != 11:
    print(f"{a} программист")
elif a % 10 in [2, 3, 4] and a % 100 != 12 and a % 100 != 13 and a % 100 != 14:
    print(f"{a} программиста")
else:
    print(f"{a} программистов")
