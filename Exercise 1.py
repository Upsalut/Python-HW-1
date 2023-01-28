# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day=int (input("Enter a number of day: "))

if day==6 or day==7:
    print("This day is a day off")
elif day<1 or day>7:
    print("This day is not a day of the week")
else: print("This day is a working day")