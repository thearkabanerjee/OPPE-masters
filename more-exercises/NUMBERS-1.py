# question statement

# Find percentage increased
# Write a function to calculate the percentage increase from the original value to the new value.

# Assume original is less than or equal to new.

# Examples

# >>> percentage_increased(50, 75)
# 50.0
# >>> percentage_increased(80, 100)
# 25.0


# template code 

# def percentage_increased(original, new):
#     '''Calculate the percentage increase from the original value to the new value.

#     Assume original is less than or equal to new.

#     Args:
#         original (float): The original value.
#         new (float): The new value.

#     Returns:
#         float: The percentage increase.

#     Examples:
#     >>> percentage_increased(50, 75)
#     50.0
#     >>> percentage_increased(80, 100)
#     25.0
#     '''
#     ...
    


def percentage_increased(original, new):
    the_difference = (new - original)
    the_percentage_increased = ((the_difference/original) * 100)

    return (the_percentage_increased)