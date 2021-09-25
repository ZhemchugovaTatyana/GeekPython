v = abs(int(input("введите целое положительное число")))
z = v % 10
while v >= 1:
     v = v // 10
     if v % 10 > z:
         z = v % 10
     if v > 9:
        continue
     else:
         print("Максимальное цифра в числе ", z)
         break