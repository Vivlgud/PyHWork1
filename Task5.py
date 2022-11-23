# 5- Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

# Пример:
# A (3,6); B (2,1) -> 5.09
# A (7,-5); B (1,-1) -> 7.21

import math
numbers1=(input('Введите через запятую координаты X и Y: '))
numbers1=numbers1.split(",")
num_x1=int(numbers1[0])
num_y1=int(numbers1[1])
numbers2=(input('Введите через запятую координаты X и Y: '))
numbers2=numbers2.split(",")
num_x2=int(numbers2[0])
num_y2=int(numbers2[1])

distance=math.sqrt((num_x2-num_x1)**2+(num_y2-num_y1)**2)
distance=round(distance,2)
print(f'Расстояние равно {distance}')
