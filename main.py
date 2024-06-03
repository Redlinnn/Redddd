import math
print("Bведите 3 коэффицента для квадратного уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("Bведите a: "))
b = float(input("Bведите b: "))
c = float(input("Bведите c: "))
D = b ** 2 - 4 * a * c
if D > 0:
    ch1 = -b + math.sqrt(D)
    x1 = (ch1 / (2 * a))
    x2 = ((-b - math.sqrt(D)) / (2 * a))
    print(f"Корень х1 = {x1} \nКорень х2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")