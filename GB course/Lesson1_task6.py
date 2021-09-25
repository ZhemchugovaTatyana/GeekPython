a = int(input("введите начальную дистанцию"))
b = int(input("введите конечную дистанцию"))
day = 1

while a < b:
    a = 1.1*a
    day += 1

print(day)

