
with open("list.txt") as file:
    file_lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        emp_info = line.split()
        employees.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
average_salary = sum_salary / len(employees)
print(f"Average = {average_salary}")

for k,v in employees.items():
    if v < 20000:
        print(f"{k}: {v}")

