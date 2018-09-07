"""
ЗАДАЧА 1
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу. Если ключа key
нет в словаре, то нужно добавить значение в список по ключу 2⋅key. Если и ключа 2⋅key нет, то нужно добавить ключ
2⋅key в словарь и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.
"""


def update_dictionary(d, key, value):
    if key in d:
        # d.setdefault(key, []).append(value)
        d[key].append(value)  # лучше сделать так, т.к мы прошли проверку и поняли, что ключ в словаре

    else:
        d.setdefault(2 * key, []).append(value)


# def timeProgram(a):
#     start = timeit.default_timer()
#     update_dictionary2(a, 2, 1)
#     stop = timeit.default_timer()
#     return stop - start


if __name__ == '__main__':
    c = {0: [1], 2: [2], 3: [3], 4: [4]}
    update_dictionary(c, 20, 3)
    print(c)

    # c.setdefault(2 * 2, []).append(6)
    # c.get(2, []).append(3)
    # print(f'время выполнения setDefault = {timeProgramSetDef(c)}')
    # print(f"время выполнения get = {timeProgramGet(c)}")
    # print(f"время выполнения проверками{timeProgram(c)}")


