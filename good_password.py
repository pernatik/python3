# объявление функции
def is_password_good(password):
    is_upper = False
    is_lower = False
    is_digit = False
    
    if len(password) < 8:
        print('False')
    else:
        for i in password:

   


# считываем данные
#txt = input()
txt = 'aabbCC11OP'
# вызываем функцию
print(is_password_good(txt))