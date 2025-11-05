# question statment


# Even Characters first and Odd Characters reversed
# Given a string, return a string with the characters in the even indices first and the characters in the odd indices next but in reversed order.

# Example For the input "abcde",

# even chars = "ace"
# odd chars = "bd"; odd chars reversed = "db"
# result = "acedb"



# template code:


# def even_first_odd_reversed(s: str) -> str:
#     '''Return a string with the characters in the even indices first 
#     and the characters in the odd indices reversed next.

#     Arguments:
#     s: str - the input string

#     Return:
#     str - modified string

#     Example:
#     >>> even_first_odd_reversed('abcde')
#     'acedb'
#     >>> even_first_odd_reversed('python')
#     'ptonhy'
#     '''
#     ...
    
def even_first_odd_reversed(s:str) -> str:
    new_string = s.split()
    index = new_string.index(char)
    for char in new_string:
        if (index % 2 != 0):
            return (char)
    


# a = even_first_odd_reversed("arka")
# print (a)



# cant solve



# solution 

    even_chars = s[::2]       # characters at even indices
    odd_chars = s[1::2][::-1]
    return even_chars + odd_chars





a = even_first_odd_reversed("arka")
print (a)