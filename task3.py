number1 = int(input("введите 1 число"))
number2 = int(input("введите  2 число"))
number3 = int(input("введите 3 число"))


if number1 < number2 < number3:
    print(number1)
elif number1 < number3 < number2:
    print(number1)
elif number2 < number1 < number3:
    print(number2)
elif number2 < number3 < number1:
    print(number2)
elif number3 < number1 < number2:
    print(number3)
elif number3 < number2 < number1:
    print(number3)
