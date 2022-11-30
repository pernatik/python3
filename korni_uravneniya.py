from math import *
# объявление функции
def solve(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        # 2 корня
        x1 = (((-b)+(d**0.5)) / (2 * a))
        x2 = (((-b)-(d**0.5)) / (2 * a))
        return (min(x1,x2)), (max(x1,x2))
    if d == 0:
        z = (-b) / (2 * a)
        return z, z
    
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)