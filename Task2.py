# 2- Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.
# not(X or Y or Z)=not X and not Y and not Z

check=0
for x in range(2):
    for y in range(2):
        for z in range(2):
            res1=int(not(x or y or z))
            res2=int(not x and  not y and not z)
            if res1==res2:
                print(f'{x} {y} {z} {res1} {res2}')
            else:
                print(f'{x} {y} {z} {res1} {res2}')
                check=1
if check==1:
    print ("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z не истинно")
else:
    print ("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  истинно")
