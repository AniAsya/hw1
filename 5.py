import random

with open("text5.txt", "w") as file:
    for _ in range(20):
        file.write(f"{random.randint(0, 10)}")

with open("text5.txt") as file:
    nums_str = file.read().split()
    sum = 0
    for num in nums_str:
        sum += int(num)

print(sum)
