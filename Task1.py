# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, 
# и что это действительно входит в нужный диапазон

# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

day_number=int(input("Введите число от 1 до 7: "))
print(type(day_number))
if 1<=day_number<=7:
    if day_number>5:
        print("Да, выходной!")
    else:
         print("Нет, не выходной:(")
else:
    print("Введено неправильное число")