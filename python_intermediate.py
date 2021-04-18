def check_score(list_of_list_param):
    result = 0
    for list_value in list_of_list_param:
        for value in list_value:
            if value == '#':
                result += 5
            elif value == 'O':
                result += 3
            elif value == 'X':
                result += 1
            elif value == '!':
                result -= 1
            elif value == '!!':
                result -= 3
            elif value == '!!!':
                result -= 5
    if result < 0:
        return 0
    else:
        return result


# Validating function

print(check_score([
    ["#", "!"],
    ["!!", "X"]
]))

print(check_score([["!!!", "O", "!"],
                   ["X", "#", "!!!"],
                   ["!!", "X", "O"]]))

print(check_score([
    ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
    ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
    ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
    ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
    ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
    ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
    ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
    ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
    ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
    ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
    ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
    ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
    ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
    ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]))

# A less optimized method
# def check_score(*arguments):
#     """Function that takes a list of lists and returns
#     the value of all of the symbols in it, where each symbol adds or takes
#     something from the total score."""
#     flat_list = []
#     for i in arguments:
#         for j in i:
#             for k in j:
#                 if k == '#':
#                     flat_list.append(5)
#                 if k == 'O':
#                     flat_list.append(3)
#                 if k == 'X':
#                     flat_list.append(1)
#                 if k == '!':
#                     flat_list.append(-1)
#                 if k == '!!':
#                     flat_list.append(-3)
#                 if k == '!!!':
#                     flat_list.append(-5)
#                 else:
#                     flat_list.append(0)
#     list_sum = sum(flat_list)
#     if list_sum < 0:
#         return 0
#     else:
#         return list_sum
