# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

numbers=(input('Введите через пробел координаты X и Y: '))
numbers=numbers.split(" ")
num_x=int(numbers[0])
num_y=int(numbers[1])
 
if num_x>0 and num_y>0:
    print('1-я четверть')
elif num_x<0 and num_y>0:
    print('2-я четверть')
elif num_x<0 and num_y<0:
    print('3-я четверть')
elif num_x>0 and num_y<0:
    print('4-я четверть')
else:
    print('Введите число отличное от 0')