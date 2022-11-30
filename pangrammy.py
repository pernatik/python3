# объявление функции
def is_pangram(text):
    s_text = sorted(set(text.lower().replace(' ', '')))
    return len(s_text) == 26
# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))