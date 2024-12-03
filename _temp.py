def find_repeated(arr):
    arrUnique = [arr[0]]
    arrRepeat = []
    for e in arr[1:]:
        if not (e in arrRepeat):
            if e in arrUnique:
                arrUnique.remove(e)
                arrRepeat.append(e)
            else:
                arrUnique.append(e)
    return arrUnique, arrRepeat

'''
print("run test --------------------------------------------------------------------")
array = []
array.append([1, 18, 2, 3, 1, 1, 3, 4, 5, 1, 5, 6, 6, 7, 8, 9, 8])
array.append([1, 2, 3, 2, 1, 3, 4, 5, 1, 5, 6, 6, 7, 9, 8])
array.append([8])
array.append([8, 8])

for a in array:
    print("Input Array\t: ", a)
    arrUnique, arrRepeat = find_repeated(a)
    print("Unique Array\t: ", arrUnique)
    print("Repeated Array\t: ", arrRepeat)
'''


def fibonacci_list(size):
    f_list = []

    def add_new_fibonacci_number(fibonacci_numbers):
        f_size = len(fibonacci_numbers)
        if f_size <= 1:
            fibonacci_numbers.append(1)
        else:
            fibonacci_numbers.append(fibonacci_numbers[f_size - 2] + fibonacci_numbers[f_size - 1])
        return fibonacci_numbers

    while len(f_list) < size:
        add_new_fibonacci_number(f_list)
    return f_list


def fibonacciRecursive(num):
    cache = [0] * num

    def fibonacci(n):
        if not n: return []
        if (n == 1):
            cache[n - 1] = 1
        elif n == 2:
            cache[n - 1] = 1
            cache[n - 2] = 1
        elif cache[n - 1] == 0:
            cache[n - 1] = fibonacci(n - 2) + fibonacci(n - 1)
        return cache[n - 1]

    fibonacci(num)
    print(cache)

'''
import timeit
num = 40

start = timeit.default_timer()
print(fibonacci_list(num))
print(timeit.default_timer() - start)

start = timeit.default_timer()
fibonacciRecursive(num)
print(timeit.default_timer() - start)

for num in range(15):
    print('n = ', num)

    start = timeit.default_timer()
    print(fibonacci_list(num))
    print(timeit.default_timer() - start)

    start = timeit.default_timer()
    fibonacciRecursive(num)
    print(timeit.default_timer() - start)

# learn more https://r-knott.surrey.ac.uk/Fibonacci/fibFormula.html
'''