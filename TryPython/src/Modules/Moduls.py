# считаем периметр круга
# def perimetr(param):
#     return param*2*math.pi
#
#
# if __name__ == '__main__':
#     print(perimetr(float(input())))


# выводим на экран все аргументы, которые ввели в консольке при запуске нашей программы
# import sys
#
# # print(*sys.argv[1:len(sys.argv)])
#
# # либо
# print(*sys.argv[1:])

# # отправляем простой get - запрос и выводим ответ в виде текста
# import requests
#
# r = requests.get("https://docs.python.org/3/library/")
# print(r.text)

# скачиваем файлик по ссылку из файла. и считаем количество строк
# import requests
# with open("dataset_3378_2.txt", "r") as f:
#     print(len(requests.get(f.read().strip()).text.splitlines()))


"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests

with open("dataset_3378_3.txt", "r") as f:
    name = requests.get(f.read().strip()).text
    while "We" not in name:
        name = requests.get(f"https://stepic.org/media/attachments/course67/3.6.3/{name}").text
        print(name)
"""