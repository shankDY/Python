# Подставляем значения x и y в данное выражение и получаем:
# 10 >5 * 5 or 10 >= 2 * 5 and 5 < 10
#
# Решаем арифметику:
#
# 10 > 25 or 10 >= 10 and 5 < 10
#
# Решаем логику:
#
# 10 > 25 = False
#
# 10>=10 = True
#
# 5 < 10 = True
#
# Получаем:
#
# False or True and True
#
# Сначала выполняем and потом or
#
# True and True = True
#
# False or True = True
x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)

# Найдите результат выражения для заданных значений a и b. Учитывайте регистр символов при ответе.
a = True
b = False
print(a and b or not a and not b)


