# объявление функции
def find_all(target, symbol):
    a = []
    for i in range(len(target)):
        if target[i] == symbol:
            a.append(i)
    return a

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all('abcdabcaaa', 'a'))