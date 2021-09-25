time_sec = int(input("Введите время в секундах"))

hour = time_sec // 3600
min = (time_sec - hour * 3600) // 60
sec = (time_sec - hour * 3600 - min * 60) % 60

print("москвоское время {} : {} : {}".format(hour, min, sec))
