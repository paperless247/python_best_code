# check if a number is negative

def is_neg(n: float) -> bool:
    return n < 0

for i in range(-2,4):
    print(i, 'is negative: ', is_neg(i))