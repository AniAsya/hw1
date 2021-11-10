def division(num_1, num_2):
    return num_1 / num_2
    '''
    Get quotient of numbers
    :param num_1: float
    :param num_2: float
    :return division: float
    '''

num_1 = float(input("Введите делимое: "))
num_2 = float(input("Введите делитель: "))
if num_2 != 0:
    print(division(num_1, num_2))
else:
    print("Делитель не может быть равен 0")




