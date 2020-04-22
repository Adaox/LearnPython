def comma(list):
    result = ""
    if len(list) == 0:
        return "Empty list"
    elif len(list) == 1:
        return f"{list[0]}"
    elif len(list) == 2:
        return f"{list[0]} and {list[1]}"
    else:
        last = list.pop()
        for i in list:
            result += f"{i}, "
        result += f"and {last}"
    return result


# Test Variables
empty = []
single = [100]
double = [1, 2]
spam = ["apples", "bananas", "tofu", "cats"]

# Test comma funciton
print(comma(empty))
print(comma(single))
print(comma(double))
print(comma(spam))
