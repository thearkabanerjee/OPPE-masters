# question statement


# Is Odd-Length Palindrome
# Write a function is_odd_length_palindrome that takes a string s and returns True if s is a palindrome of odd length, and False otherwise.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

#     • "hello" --> False (not a palindrome)

#     • "noon" --> False (palindrome but not odd length)

#     • "nun" --> True (palindrome and odd length)



# sample code / template code :

def is_odd_length_palindrome(s: str) -> bool:
    '''Check if a string is a palindrome with odd length.

    Args:
        s : str - input string

    Returns:
        bool - True if s is a palindrome with odd length, False otherwise.
    '''
    ...




def is_odd_length_palindrome(s:str)-> bool:
	if (len(s) % 2 == 0):
		return False
	else:
		if ((s[::-1]) == s):
			return True 
		else:
			return False

s = is_odd_length_palindrome("madan")
print (s)



# the top 1% of the 1% . the guys who get to play god without permission.