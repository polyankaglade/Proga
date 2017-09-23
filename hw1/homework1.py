# Три числа
# a и b в сумме дают c
# c является решением линейного уравнения ax + b = 0



a = int(input('Enter the first number (A): '))
b = int(input('Enter the second number (B): '))
c = int(input('Enter the third number (C): '))
print("\n")

if a  + b == c:
  print('The third number is the sum of the first two.', end='\n\n')
else:
  print('The third number is NOT the sum of the first two', end='\n\n')
  
print('Equasion: ax+b=0 .')
  
if (a*c)+b == 0:
  print('The third number is the root of this equasion.')
else:
  print('The third number is NOT the root of this equasion.')
