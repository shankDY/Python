
"""Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое
частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:

abc a bCd bC AbC BC BCD bcd ABC
Sample Output:

abc 3
"""

# # c применением ламбда выражения
with open("dataset_3363_3.txt", "r") as f:
    r = f.read().replace("\n", "").lower().split()
b = {item: r.count(item) for item in r}
keyWithMaxValue = max(b.keys(), key=(lambda k: b[k]))
maxValue = b.setdefault(keyWithMaxValue)
print(f"{keyWithMaxValue} {maxValue}")


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
