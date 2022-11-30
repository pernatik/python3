# объявление функции
def draw_triangle():
    for i in range(1, 9):
        if i == 1:
            print(f'{" " * (8 - i)}*')
        if i > 1:
            print(f'{" " * (8 - i)}{"*"*((i*2)-1)}')
        

# основная программа
draw_triangle()  # вызов функции