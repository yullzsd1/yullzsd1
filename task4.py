numbers = [4, 6, 55665, 222, 8]
max_element = numbers[0]

for i in numbers:
    if i >= max_element:
        max_element = i
print("Самый большой Элемент", max_element)