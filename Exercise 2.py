# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = True
y = True
z = True

if not(x or y or z) == (not x and not y and not z):
    print('Expression is true.')
else:
    print('Expression is false.')