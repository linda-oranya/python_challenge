def check_score(*arguments):
    """Function that takes a list of lists and returns
    the value of all of the symbols in it, where each symbol adds or takes
    something from the total score."""
    flat_list = []
    for i in arguments:
        for j in i:
            for k in j:
                if k == '#':
                    flat_list.append(5)
                if k == 'O':
                    flat_list.append(3)
                if k == 'X':
                    flat_list.append(1)
                if k == '!':
                    flat_list.append(-1)
                if k == '!!':
                    flat_list.append(-3)
                if k == '!!!':
                    flat_list.append(-5)
                else:
                    flat_list.append(0)
    list_sum = sum(flat_list)
    if list_sum < 0:
        return 0
    else:
        return list_sum


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
