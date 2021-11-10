def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    min_num = min(my_list)
    my_list.remove(min_num)
    return my_list[0] + my_list[1]
    '''
    Get summ of two biggest numbers
    :param num_1: int
    :param num_2: int
    :param num_3: int
    :param my_list: list
    :param min_num: int
    :return: my_func: int
    '''

print(my_func(9, 18, 98))
