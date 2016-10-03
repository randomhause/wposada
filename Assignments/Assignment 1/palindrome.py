#Question 2

""" The palindrome function takes a string & returns TRUE if the string is a palindrome and FALSE
    if it is not:
        (1) If the string has a length of 1 or 0, it'll be the stop value on the recursion. 
        (2) If the outer characters are the same, it'll run the palindrome function on the middle
            of the string (but exclude the outer characters).
        (3) If the outer characters are not the same, the string is not a palindrome. """

def word(): 
    inputStr = input('Please enter a word: ')
    if is_palindrome(inputStr):
        print("That is a palindrome.")
    else:
        print("That is not a palindrome.")

def is_palindrome(my_string): 
    if len(my_string) <= 1: 
        return True 
    elif my_string[0] == my_string[len(my_string) - 1]:
        return is_palindrome(my_string[1:len(my_string) - 1])
    else:
        return False

word()
 