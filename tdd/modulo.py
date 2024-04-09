def sumar(numeros):
    res = 0
    s = ''
    for c in numeros:
        if c == ',':
            res += int(s)
            s = ''
        else:
            s += c
    if s != '':
        res += int(s)
    return res
