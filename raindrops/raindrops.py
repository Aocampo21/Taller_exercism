
def convert(number):
    dic = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    factors = [dic[x] for x in [3, 5, 7] if number % x == 0]
    return str(number) if len(factors) == 0 else ''.join(factors)
