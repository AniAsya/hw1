number = int(input("Введите любое целое положительное число: "))
max_num = 0
while number > 0:
    if number % 10 > max_num:
        max_num = number % 10
        if max_num == 9:
            break
    number //= 10

print(f"Максимальная цифра числа: {max_num}")

