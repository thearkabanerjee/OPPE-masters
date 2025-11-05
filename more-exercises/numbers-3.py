
# Arithmetic Operations tuple from two integers
# Given a tuple of two integers (a, b), return a tuple containing the sum, difference, product, and quotient (integer division) of the two numbers.
# Example:

# >>> arithmetic_operations((1, 2))
# (3, -1, 2, 0)

# def arithmetic_operations(t: tuple) -> tuple:
#     '''
#     Given a tuple of two integers (a, b), return a tuple containing the 
#     sum, difference, product, and quotient (integer division) of the two numbers.

#     Arguments:
#     t: tuple - a tuple of two integers (a, b)

#     Return:
#     tuple - a tuple containing the sum, difference, product, and quotient

#     Example:
#     >>> arithmetic_operations((1, 2))
#     (3, -1, 2, 0)
#     '''
#     ...
    


def arithmetic_operations(t:tuple) -> tuple:
    s = sum(t)
    difference = t[0] - t [1]
    product = t[0] * t[1]
    quotient = t[0] //t[1]
    return (s, difference, product, quotient)


a= arithmetic_operations((10, 5))
print (a)