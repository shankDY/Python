"""Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и
выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output:

Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
"""
# import itertools
#
# n = int(input('kolichestvo igr: '))
# x_list = [input('kom1;gol1;kom2;gol2: ').split(';') for x in range(n)]
# vs = [(x[0], x[2]) for x in x_list]
#
# clubs = set(itertools.chain.from_iterable(vs))
# res = {club: [0, 0, 0, 0, 0] for club in clubs}
# for kom1, gol1, kom2, gol2 in x_list:
#     res[kom1][0] += 1
#     res[kom2][0] += 1
#     if int(gol1) > int(gol2):
#         res[kom1][1] += 1
#         res[kom1][4] += 3
#         res[kom2][3] += 1
#     elif int(gol1) < int(gol2):
#         res[kom2][1] += 1
#         res[kom2][4] += 3
#         res[kom1][3] += 1
#     elif int(gol1) == int(gol2):
#         res[kom1][2] += 1
#         res[kom1][4] += 1
#         res[kom2][2] += 1
#         res[kom2][4] += 1
# for club in clubs:
#     print('{}:{}'.format(club, ' '.join(map(str, res[club]))))


# таже задача , но со словарем и использование zip

d = {}
for a, p, b, v in (input().split(';') for n in range(int(input()))):
    d[a] = [i + j for i, j in
            zip(d.setdefault(a, [0, 0, 0, 0, 0]), [1, (p > v), (p == v), (p < v), 3 if p > v else (p == v)])]
    d[b] = [i + j for i, j in
            zip(d.setdefault(b, [0, 0, 0, 0, 0]), [1, (p < v), (p == v), (p > v), 3 if p < v else (p == v)])]
print(*(i + ":" + ' '.join(map(str, d.get(i))) for i in d), sep='\n')
