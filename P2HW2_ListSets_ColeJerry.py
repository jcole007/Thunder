# CTI-110
# P2HW2 - List and Sets
# Jerry Cole 
# 3/4/2021
# Asks the user to enter a series of 10 numbers.
# The program should store the numbers in a list.
# Give the list created a descriptive name.
number1 = int(input('Enter number: '))
number2 = int(input('Enter number: '))
number3 = int(input('Enter number: '))
number4 = int(input('Enter number: '))
number5 = int(input('Enter number: '))
number6 = int(input('Enter number: '))
number7 = int(input('Enter number: '))
number8 = int(input('Enter number: '))
number9 = int(input('Enter number: '))
number10 = int(input('Enter number: '))
number_list = (number1, number2, number3, number4, number5, number6, number7,\
               number8, number9, number10)
print('The list of number',number_list)
#Display the output of number.

print('The lowest number:', min(number_list))
print('The highest number:', max(number_list))
print('The total number', len(number_list), 'in the list.')
print('The average number:', sum(number_list))
input('Press Enter to exit. ')





