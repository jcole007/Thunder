# Count input length without spaces, periods, ecclamation \n
# points, or commas.
# Date 3/29/2021
# P4LAB1_InputLength_ColeJerry
# ask user_text input.
# used loop for and if Boolean expression.
# print count.

def main():
    user_text = input()
    count = 0
    for text in user_text:
        if not(text in " .,!"):# The not Operator.
            count +=1
    print(count)

main()

