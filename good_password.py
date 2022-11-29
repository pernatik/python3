# объявление функции
def is_password_good(password):
    is_upper = False
    is_lower = False
    is_digit = False
    
    if len(password) < 8:
        return False
    else:
        for i in password:
            if i.isupper() == True:
                is_upper = True
            elif i.islower() == True:
                is_lower = True
            elif i in '0123456789':
                is_digit = True
        if is_digit == True and is_lower == True and is_upper == True:
            return True
        else:
            return False

# считываем данные
txt = input()
#txt = 'aaAA12qqp'
# вызываем функцию
print(is_password_good(txt))