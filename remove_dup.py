# Question 10: Write a Python program to remove duplicates from a list.

def remove_dup(L: list) -> list:
    res = []
    for e in L:
        if e not in res:
            res.append(e)
    return res

# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_dup(nums)
print(unique_nums)

# Use set()
print(list(set(nums)))