time = int(input("Введите время в секундах: "))
if time < 60:
    print(f"00:00:{time:02}")
elif time < 3600:
    print(f"00:{time // 60:02}:{time % 60:02}")
else:
    print(f"{time // 3600:02}:{(time // 3600) // 60:02}:{time % 60:02}")
