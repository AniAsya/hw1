
num = int(input("Введите любое целое положительное число: "))
my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
for item in my_list:
    while int(item) <= num:
        a = my_list.index(item)
        my_list.insert(a, num)
    print(my_list)
    break



