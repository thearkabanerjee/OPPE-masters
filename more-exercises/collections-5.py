# problem statement



# def common_char_sorted_str(s1:str, s2:str) -> str: 
#     '''Returns a sorted string with unique common charecters present in the given strings.

#     Arg:
#         s1 (str) : Input string. 
#         s2 (str) : Input string. 

#     Returns: 
#         str: string of unique common charecters arranged in ascending order. 

#     Examples:
#     >>> common_char_sorted_str('apple', 'ball')
#     'al'
#     >>> common_char_sorted_str('abcde', 'edfci')
#     'cde'
#     '''
#     ...
    


def common_char_sorted_str(s1:str, s2:str) -> str: 
    common_character_string = set(s1) & set(s2)
    sort_kardo = sorted(common_char_sorted_str)
    return sort_kardo


a = common_char_sorted_str("apple", "ball")
print(a)