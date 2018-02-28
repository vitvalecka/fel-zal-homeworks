def polyEval(poly, x):
    délka = len(poly)
    i = 0
    výsledek = 0
    while i < délka:
        výsledek += poly[i] * (x ** i)
        i += 1
    return výsledek


def polySum(poly1, poly2):
    délka1 = len(poly1)
    délka2 = len(poly2)
    výsledek = []
    i = 0
    if délka1 < délka2:
        while i < délka1:
            výsledek.append(poly1[i] + poly2[i])
            i += 1
        while i < délka2:
            výsledek.append(poly2[i])
            i += 1
    else:
        while i < délka2:
            výsledek.append(poly1[i] + poly2[i])
            i += 1
        while i < délka1:
            výsledek.append(poly1[i])
            i += 1
    i = len(výsledek) - 1
    while výsledek[i] == 0:
        del výsledek[i]
        i -= 1
    return výsledek


def polyMultiply(poly1, poly2):
    délka1 = len(poly1)
    délka2 = len(poly2)
    výsledek = []
    i = 0
    j = 0
    while i < ((délka1-1) * (délka2-1)):
        výsledek.append(0)
        i += 1
    i = 0
    while i < délka1:
        while j < délka2:
            výsledek[i+j] += poly1[i] * poly2[j]
            j += 1
        i += 1
        j = 0
    i = (len(výsledek) - 1)
    while výsledek[i] == 0:
        del výsledek[i]
        i -= 1
    return výsledek
