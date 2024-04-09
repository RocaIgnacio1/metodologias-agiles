def sumar(numeros):
    start = 0
    sep = ','
    res = 0
    s = ''
    if numeros.startswith('//') and numeros[3] == '\n':
        sep = numeros[2]
        start = 4
    for c in numeros[start:]:
        if c in [sep, '\n']:
            res += int(s)
            s = ''
        else:
            s += c
    if s != '':
        res += int(s)
    return res
