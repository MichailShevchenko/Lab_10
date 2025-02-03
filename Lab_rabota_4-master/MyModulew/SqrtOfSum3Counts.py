import math

x = int(input("Введите число 1: "))
y = int(input("Введите число 2: "))
z = int(input("Введите число 3: "))


def f(x, y,z):
    a = x + y + z
    return math.sqrt(a)


print("Квадратный корень их суммы: ", f(x, y, z))

