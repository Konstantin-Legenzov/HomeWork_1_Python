# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

import math


a =[]  
for i in list(input()):
    a.append(int(i))
print(a)

b =[]  
for i in list(input()):
    b.append(int(i))
print(b)

rasstoyanie = math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]))
finish_result = float(round(rasstoyanie, 3))
print(finish_result)