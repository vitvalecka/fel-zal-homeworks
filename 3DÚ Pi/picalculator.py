import math


def newtonPi(init):
    nové = init
    předešlé = 0
    while math.fabs(předešlé - nové) > 0.000000001:
        předešlé = nové
        nové = předešlé - (math.sin(předešlé) / math.cos(předešlé))
    return nové


def leibnizPi(iterations):
    i = 1
    počítadlo = 0
    výsledek = 0
    while počítadlo < iterations:
        foo = 4 / i
        if počítadlo % 2 == 1:
            foo *= (-1)
        výsledek += foo
        počítadlo += 1
        i += 2
    return výsledek


def nilakanthaPi(iterations):
    if iterations == 1:
        return 3
    else:
        i = 3
        počítadlo = 1
        výsledek = 3
        while počítadlo < iterations:
            foo = 4 / ((i - 1) * i * (i + 1))
            if počítadlo % 2 == 0:
                foo *= (-1)
            výsledek += foo
            počítadlo += 1
            i += 2
        return výsledek


print(newtonPi(-3))
