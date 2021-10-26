distance = float(input("Введите результат за первый день: "))
days = 1
goal = float(input("Введите целевое значение: "))
while distance < goal:
    distance *= 1.1
    days += 1

print(f"Спортсмену потребуется {days} дней")
