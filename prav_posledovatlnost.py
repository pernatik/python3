# объявление функции
def is_correct_bracket(text):
    count = 0
    if not len(text)%2 == 0 or text[0] == ')' or text[-1] == '(':
        return False
    else:
        for i in text:
            if i == '(':
                count = count + 1
            elif i == ')':
                count = count - 1
            while count < 0:
                return False
                break
        return True
# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
