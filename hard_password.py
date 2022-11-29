# объявление функции
def is_valid_password(password):
    spisok = []
    spisok = password.split(':')
    if not len(spisok) == 3:
        return False
    else:
        
        a = spisok[0]
        b = int(spisok[1])
        c = int(spisok[2])
        aflag = False
        bflag = False
        cflag = False
        # Polindrom
        if a == a[::-1]:
            aflag = True
        k = 0
        for i in range(2, b // 2+1):
            if (b % i == 0):
                k = k+1
        if (k <= 0):
            bflag = True
        # Четность
        if c % 2 == 0:
            cflag = True
        
        return aflag == True and bflag == True and cflag == True

# считываем данные
#psw = '1221:101:22'
psw = input()

# вызываем функцию
print(is_valid_password(psw))