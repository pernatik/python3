import math

# объявление функции
def get_circle(radius):    
    p = math.pi
    c = 2 * p * r
    s = p * (r * r)
    return c, s
# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)