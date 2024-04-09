def sumar(numeros):
    start = 0
    sep = ','
    res = 0
    s = ''
    if numeros.startswith('//') and numeros[3] == '\n':
        sep = numeros[2]
        start = 4
    nums = []
    for sub in numeros[start:].split(sep):
        for n in sub.split('\n'):
            if n != '':
                nums.append(n)
    return sum([int(n) for n in nums])
