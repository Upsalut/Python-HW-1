# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

print('Enter point coordinates:')
x = int(input('Eter a coordinate X: '))
y = int(input('Eter a coordinate Y: '))

if x == 0 or y == 0:
    print('One or more coordinates has the value equals zero!!')
else:
    if   x > 0 and y > 0: print('This point is in 1 quarter') 
    elif x < 0 and y > 0: print('This point is in 2 quarter')  
    elif x < 0 and y < 0: print('This point is in 3 quarter')
    else:                 print('This point is in 4 quarter')