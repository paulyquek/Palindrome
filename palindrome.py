# To be run with one argument, as "python palindrome.py '<test_string>',"
# Where test_string is to be tested whether it is a palindrome
import string
import sys

test_string = sys.argv[1]
stripped_string_list = []
# Removes all non-alphabetic characters, making all of it a list
for i in range(len(test_string)):
    if test_string[i] in string.ascii_letters:
         stripped_string_list.append(test_string[i])
# Changes the list into a string, and turns all lowercase. rev_string reverses
# the list first.
stripped_string = ''.join(stripped_string_list).lower()
rev_string = ''.join(stripped_string_list[::-1]).lower()

if stripped_string == rev_string:
    print(test_string, 'is a palindrome.')
else:
    print(test_string, 'is not a palindrome.')
