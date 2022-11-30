# объявление функции
def is_magic(date):
    d,m,g=map(int,date.split('.'))
    g=g%100
    return d * m == g

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))