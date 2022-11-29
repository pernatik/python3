# объявление функции
def is_palindrome(text):
    text1="".join(i for i in text if i.isalpha())
    a = text1.lower()
    #return text1.lower()
    b = a[::-1]
    return a == b
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))