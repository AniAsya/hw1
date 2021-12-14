my_list = [8, 90, 7, 352, 78, 79, 89, 56, 5, 68]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)