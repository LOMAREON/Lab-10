def N_Check():  # обработчик ошибки ввода числа i
    while True:
        try:
            N = int(input("Введите сумму, которую нужно уплатить: "))
            return N
        except ValueError:
            print("Нужно ввести цифру!")

Bank = [64, 32, 16, 8, 4, 2, 1]
k = [0] * 7
N = N_Check()
a = N
i = 0
while N != 0:
    if N > Bank[i] or N == Bank[i]:
        N = N - Bank[i]
        k[i] += 1
    else:
        i += 1
print ('Для уплаты суммы ' + str(a) + ' вам нужно заплатить: ')
print (str(k[0]) + ' купюр(ы) номеналом 64')
print (str(k[1]) + ' купюр(ы) номеналом 32')
print (str(k[2]) + ' купюр(ы) номеналом 16')
print (str(k[3]) + ' купюр(ы) номеналом 8')
print (str(k[4]) + ' купюр(ы) номеналом 4')
print (str(k[5]) + ' купюр(ы) номеналом 2')
print (str(k[6]) + ' купюр(ы) номеналом 1')
