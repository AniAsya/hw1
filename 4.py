my_str = input("Введите несколько слов через пробел: ")
my_list = list(my_str.split())

for item in enumerate(my_list):
    print(str(item)[0:15])


