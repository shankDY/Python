"""

Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667
У вас есть неограниченное число попыток.

"""

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