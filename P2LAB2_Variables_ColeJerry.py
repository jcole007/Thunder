# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
# FIXME (2): Output the four values in reverse
# FIXME (3): Convert the integer to a characer, and output that character
# ENTER INTERGER 32 - 126.
#Enter the Float value of 3.77
# Enter the character input z.
# Enter the string Howdy
# Output integer, float, chatacter and string.
# Reverse the output
# output a character statement.
# Character for alphabet range from 0-25 0=a 25=z.

user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float :\n'))
user_char = input('Enter character :\n ')
user_string = input('Enter String :\n ')
characer = user_int
alphabet = 'abcdefghijklmnopqrstuvwxyz'
user_number = int(input('Enter number 0 - 25 for character: '))
print ("""Enter float:
Enter character:
Enter string:""")
print(user_int, user_float, user_char, user_string)
print(user_string, user_char, user_float, user_int)
print(characer, 'converted to a character is', alphabet[user_number])


      
