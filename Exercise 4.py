# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
coor_part = int(input("Enter a quarter part: "))

if coor_part==1: print("This part includes x from 0 to infinity and y from 0 to infinity")
elif coor_part==2: print("This part includes x from 0 to negative infinity and y from 0 to infinity")
elif coor_part==3: print("This part includes x from 0 to negative infinity and y from o to negative infinity")
elif coor_part==4: print("This part includes x from 0 to infinity and y from 0 to negative infinity")
else: print("This part of coordinates is not exist")