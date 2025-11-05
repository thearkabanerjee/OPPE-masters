# palindrome number :


# Palindrome Integer
# Given an integer, check whether it is a palindrome. A palindrome is a number or a string that reads the same backward as forward.

# Assume the numbers are positive.

# Example

# is_palindrome(121) == True
# is_palindrome(123) == False
# is_palindrome(1212) == False


# template code :


# def is_palindrome(n: int) -> bool:
#     '''Checks if an integer is a palindrome.

#     Arguments:
#     n: int - the integer to check

#     Return:
#     bool - True if the integer is a palindrome, False otherwise
#     '''
#     ...
    


def is_palindrome(n: int)-> bool:
    string_n = str(n)
    palindrome = string_n[::-1]
    if (string_n == palindrome):
        return True
    else :
        return False