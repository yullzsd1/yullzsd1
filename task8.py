import random

randoms = random.randint(1, 101)

while True:
    number = int(input('введи загаданное число'))
    if number < randoms:
        print('ваше число меньше загаданного')
    elif number > randoms:
        print('ваше число больше')
    elif number == randoms:
        print('вы угадали!!!!!!')
        break