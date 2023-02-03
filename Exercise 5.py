# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

def get_coordinates(text): # The function for getting coordinates to the list
    list = []
    list.append(int(input(f'Enter X coordinate {text} point: ')))
    list.append(int(input(f'Enter Y coordinate {text} point: ')))
    return list
#-----------------------------------------------------------------------------------------------------------------------------------+
print('Enter points coordinates.')
first_point_coords  = get_coordinates('first')
second_point_coords = get_coordinates('second')

result = math.sqrt((first_point_coords[0] - second_point_coords[0])**2 + (first_point_coords[1] - second_point_coords[1])**2)

print(f'Distance between two points equals {result}')