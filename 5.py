proceeds = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))
profit = proceeds - costs

if profit < 0:
        print("Ваша фирма работает в убыток")
elif profit == 0:
        print("Ваша фирма компенсирует затраты, но не имеет прибыли")
else:
        print("Ваша фирма работает с прибылью")

if profit > 0:
    profitability = profit / proceeds
    print(f"Рентабельность: {profitability}")
    amount = int(input("Введите количество сотрудников: "))
    profit_am = profit / amount
    print(f"Прибыль Вашей фирмы в расчете на одного сотрудника: {profit_am}")



