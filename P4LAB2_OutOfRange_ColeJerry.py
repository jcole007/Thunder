#P4LAB2_OutOfRange_coleJerry
#Date 4/1/2021
#Using if and while loop.
#Enter the first number.
def main():
    first_Num = int(input('Enter the first number: '))
#Enter the second number.
    second_Num = int(input('Enter the second number: '))
    if first_Num > second_Num:
        print("Second integer can't be less than the first. ")
    while first_Num <= second_Num:
        print(first_Num, end='  ')
        first_Num = first_Num + 5

main()

