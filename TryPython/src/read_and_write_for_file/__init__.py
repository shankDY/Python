"""
l = [str(i) + str(i - 1) for i in range(20)]
print(l)

# запишим данный список в файл
# открываем файл для записи, если он существует, все перезапишется, если его нет, он будет создан
f = open("c:/Users/Shank/Downloads/file.txt", "w")
for item in l:
    # записываем элементы списка в файл, каждый на новой строке(для этого надо явно указать служебный символ \n)
    f.write(f"{item}\n")
# закрываем файл(в ручном режиме), освождая ресурсы
f.close()
# данный кусок кода не запустится , т.к поток закрыт
#чтобы записать число, его надо явно перевести в строку
f.write(str(1))
"""

"""
# тот же пример, но с применением whith, который автоматически закроет нам файл

l = [str(i) + str(i - 1) for i in range(20)]
print(l)

# запишим данный список в файл
# открываем файл для записи, если он существует, все перезапишется, если его нет, он будет создан
# т.к применен оператор with, то нам не надо париться на счет закрытия файла, после проделанной операции
with open("c:/Users/Shank/Downloads/file.txt", "w") as f:
    for item in l:
        # записываем элементы списка в файл, каждый на новой строке
        f.write(f"{item}\n")
# данный кусок кода не запустится , т.к находится за границей блока whith, и файл уже закрыт
f.write("adadad")
"""

"""
# чтение из файла
path = "c:/Users/Shank/Downloads/file.txt"
with open(path, "r") as f:
    # чтение всего файла целиком
    #r = f.read()
    #построчное чтение
    for r in f:
        r = r.strip()
        print(r)
"""

""" 

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования 
повторов, и производит обратную операцию, получая исходный текст. 

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка 
"download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на 
компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у 
вас получится, надо отправить в качестве ответа на эту задачу. 

Sample Input:

a3b4c2e10b1
Sample Output:

aaabbbbcceeeeeeeeeeb


# with open("dataset_3363_2.txt", "r") as f:
#     r = f.read().strip()
#     print(r)
#     l = len(r) - 2
#     t = ''
#     for i in range(0, l):
#         if r[i + 1].isdigit() and r[i + 2].isdigit():
#             t = t + r[i] * int(r[i + 1] + r[i + 2])
#         elif r[i].isalpha():
#             t = t + r[i] * int(r[i + 1])
#     print(t)


# таже программа , но с регуляркой
import re

with open("dataset_3363_2.txt", "r") as f:
    r = f.read().strip()
ciphra = re.findall("\d+", r)
bukva = re.findall("\D+", r)
for i in range(len(bukva)):
    print("".join(bukva[i] * int(ciphra[i])), end="")
"""


# # c применением ламбда выражения
# with open("dataset_3363_3.txt", "r") as f:
#     r = f.read().replace("\n", "").lower().split()
# b = {item: r.count(item) for item in r}
# keyWithMaxValue = max(b.keys(), key=(lambda k: b[k]))
# maxValue = b.setdefault(keyWithMaxValue)
# print(f"{keyWithMaxValue} {maxValue}")

#
# # стандарьным перебором
# with open("dataset_3363_3.txt", "r") as f:
#     r = f.read().replace("\n", "").lower().split()
# y = 0
# m = " "
# for i in r:
#     z = r.count(i)
#     if z > y:
#         y = z
#         m = i
#     elif z == y and i < m:
#         m = i
# print(m, y)

def meanAllStudents(spisok):
    suma = 0
    for items in spisok:
        suma += int(items)
    return suma / len(spisok)


mat = []
phiz = []
rush = []
with open("dataset_3363_4.txt", "r") as f:
    for r in f:
        r = r.strip().split(";")
        mat.append(r[1])
        phiz.append(r[2])
        rush.append(r[3])
meanMath = meanAllStudents(mat)
meanPhiz = meanAllStudents(phiz)
meanRush = meanAllStudents(rush)

for i in range(len(mat)):
    print((int(mat[i])+int(phiz[i])+int(rush[i]))/3)

print(meanMath, meanPhiz, meanRush, end=" ")
