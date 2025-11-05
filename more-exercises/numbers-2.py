# question statement


# Check if ten digit even number
# Write a function to check if a number is a ten-digit even number.
# Also account for negative numbers discarding the sign.

# Examples

# >>> is_ten_digit_even(8769473839)
# False
# >>> is_ten_digit_even(928948)
# False
# >>> is_ten_digit_even(9289479278)
# True
# >>> is_ten_digit_even(-9289479278)
# True


#template code 

# def is_ten_digit_even(n):
#     '''Checks if a number is a 10 digit even number.

#     Also account for negative numbers discarding the sign.

#     Args: 
#         n (int): The given number. 
    
#     Returns: 
#         bool : result as True or False. 
    
#     Examples:
#     >>> is_ten_digit_even(8769473839)
#     False
#     >>> is_ten_digit_even(928948)
#     False
#     >>> is_ten_digit_even(9289479278)
#     True
#     >>> is_ten_digit_even(-9289479278)
#     True
#     '''
#     ...
    
# print (bool(0)). -> prints out False 

# print (bool (1)) -> prints out True

def is_ten_digit_even(n):
    if (n % 2 == 0):
        n = str(n)
        if (len(n)==10):
         return (bool(1))
        else:
           return (bool(0))
    else: 
        return (bool (0))
    



a = is_ten_digit_even(-1212121212)
print (a)