# Игра угадайка
import math 
import random as r

## Функции

# Защита от дурака
def is_valid(x):
    return 0 < x < 101

# Программа
num = r.randint(1,100)
print('Добро пожаловать в числовую угадайку')
print(num)
while True:
    user_num = int(input())
    if is_valid(user_num) == True:
        
        if user_num < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        if user_num > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        if user_num == num:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

    else:
        print('А может быть все-таки введем целое число от 1 до 100?')


#print(is_valid(num))
#print (math.ceil(math.log2(20)))
