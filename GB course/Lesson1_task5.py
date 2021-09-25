net = float(input("Введите значение выручки"))
charge = float(input("Введите значение издержек"))
profit = net - charge
rent = profit / net

if profit > 0:
    print("фирма получила прибыль")
    print("рентабельность составляет", rent)
    stuff = int(input("укажите количество сотрудников фирмы"))
    profitind = profit / stuff
    print("прибыль на одного сотрудника =", profitind)
    print("completed")

if profit < 0:
    print("фирма работала в убыток")
