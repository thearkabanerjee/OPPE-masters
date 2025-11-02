# question statement

# Sum of squares and absolute difference of squares
# Write a function sum_squares_abs_diff_squares that takes two integer inputs, a and b, and returns a tuple with:

#     1. The sum of the squares of a and b.

#     2. The absolute difference of the squares of a and b.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example
# Given the inputs a = 3 and b = 4:

# Explanation

#     • The sum of squares would be 9 + 16 = 25.

#     • The absolute difference of squares would be |9 - 16| = 7.

# So, sum_squares_abs_diff_squares(3, 4) should return (25, 7).




# sample code /template code:

def sum_squares_abs_diff_squares(a:int, b:int) -> tuple:
    '''Return the sum of squares and the absolute difference of squares.

    Args:
        a, b : int - input numbers

    Returns:
        tuple - tuple with sum of squares and absolute difference of squares.

    '''
    ...
    



def sum_squares_abs_diff_squares(a:int, b:int) -> tuple:
	square_of_a = (a**2)
	square_of_b = (b**2)
	sum_of_the_squares = square_of_a + square_of_b
	abs_diff_sqa_sqb= abs(square_of_a - square_of_b)
	return (sum_of_the_squares, abs_diff_sqa_sqb)


a = sum_squares_abs_diff_squares(3, 4)

print (a)










