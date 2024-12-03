import et


def factors_to_value(F:dict) -> int:
    '''factors in dict to value'''
    re = 1
    for f in F:
        re *= f**F[f]
    return re


def gcf(a:list, b:list) -> dict:
    ''' greatest common factor '''
    re = {}
    for i in a:
        if i in b:
            re[i] = min(a[i], b[i])
    if not len(re):
        return {1:1}
    return re


def lcm(a:list, b:list) -> dict:
    ''' least common multiple '''
    S = set(list(a.keys()) + list(b.keys()))
    re = {}
    for i in S:
        if i not in a:
            re[i] = b[i]
        elif i not in b:
            re[i] = a[i]
        else:
            re[i] = max(a[i], b[i])
    return re


a, b = 450, 26460

print(a, af := et.prime_factor_dict(a))
print(b, bf := et.prime_factor_dict(b))
print(lcm := lcm(af,bf), factors_to_value(lcm))
print(gcf := gcf(af,bf), factors_to_value(gcf))