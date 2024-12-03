# Question 9: Write a Python program to find the second largest number in a list.

def find_second_largest(L: list) -> int:
    a, b = 0, 1
    for e in L:
        if a < e < b:
            a = e
        elif b < e:
            a, b = b, e
    return a

# Test the function
nums = [10, 5, 8, 20, 3]
second_largest_num = find_second_largest(nums)
print(f"The second largest number is {second_largest_num}")