# объявление функции
def convert_to_python_case(text):
    snake_r = ''
    for i in range(len(text)):
        if i == 0:
            snake_r = snake_r + text[0].lower()
        elif text[i].islower():
            snake_r = snake_r + text[i]
        elif text[i].isupper():
            snake_r = snake_r + '_'+ text[i].lower()
        elif text[i].isdigit():
            snake_r = snake_r + text[i]
            
    return snake_r
  
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
