def sortNumbers(weights, condition):
    délka = len(weights)
    prohozeno = True
    foo = 0
    if condition == 'ASC':
        while prohozeno == True:
            prohozeno = False
            i = 1
            while i < (délka):
                if weights[i-1] > weights[i]:
                    foo = weights[i-1]
                    weights[i-1] = weights[i]
                    weights[i] = foo
                    prohozeno = True
                i += 1
    elif condition == 'DESC':
        while prohozeno == True:
            prohozeno = False
            i = 1
            while i < (délka):
                if weights[i-1] < weights[i]:
                    foo = weights[i-1]
                    weights[i-1] = weights[i]
                    weights[i] = foo
                    prohozeno = True
                i += 1

    return weights


def sortData(weights, data, condition):
    délka1 = len(weights)
    délka2 = len(data)

    if délka1 != délka2:
        raise ValueError('Invalid input data')

    prohozeno = True
    fooNum = 0
    fooData = ''
    if condition == 'ASC':
        while prohozeno == True:
            prohozeno = False
            i = 1
            while i < (délka1):
                if weights[i - 1] > weights[i]:
                    fooNum = weights[i - 1]
                    fooData = data[i - 1]
                    weights[i - 1] = weights[i]
                    data[i - 1] = data[i]
                    weights[i] = fooNum
                    data[i] = fooData
                    prohozeno = True
                i += 1
    elif condition == 'DESC':
        while prohozeno == True:
            prohozeno = False
            i = 1
            while i < (délka1):
                if weights[i - 1] < weights[i]:
                    fooNum = weights[i - 1]
                    fooData = data[i - 1]
                    weights[i - 1] = weights[i]
                    data[i - 1] = data[i]
                    weights[i] = fooNum
                    data[i] = fooData
                    prohozeno = True
                i += 1

    return data
