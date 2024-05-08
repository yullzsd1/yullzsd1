my_list = [2, -6, 8, 55]
start_index = 0


while True:
    if my_list[start_index] < 0:
        print("Отрицательное число есть!")
        break

    start_index = start_index + 1
