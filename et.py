# most common codes

def count_e(L:list) -> dict:
    ''' count all elements in a list '''
    re = {}
    for e in L:
        if e in re:
            re[e] += 1
        else:
            re[e] = 1
    return re


def count_i(L:list, *k) -> dict:
    ''' count element k(s) in a list '''
    re = {i:0 for i in k}
    for e in L:
        if e in re:
            re[e] += 1
    return re


def prime_factor(n:int, start:int=2) -> list:
    factors = []
    for i in range(2, n):
        if not (n % i):
            factors.append(i)
            for j in prime_factor(n//i, i):
                factors.append(j)
            break
    else:
        factors.append(n)
    return factors


def prime_factor_dict(n:int) -> dict:
    return count_e(prime_factor(n))


def product(L:list) -> int:
    ''' product of all elements in the list '''
    re = 1
    for e in L:
        re *= e
    return re




# some very basic useful functions

def dir_(var):
    '''
        input: a variable
        output: its type and dir
    '''
    print(type(var), [ i for i in dir(var) if not i.startswith('__') ])


class list_(list):
    ''' add more functions to a list '''

    def freq_(self):
        return count_e(self)
    
    def unique_(self):
        re = self.freq_()
        return [int(k) for k in re if re[k] == 1]

    def repeat_(self):
        re = self.freq_()
        return [int(k) for k in re if re[k] >  1]