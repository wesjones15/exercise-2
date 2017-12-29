def evenDivisors(min, max, divisor):
    returnList = []
    for i in range (min, max+1):
        if (i % divisor == 0):
            returnList.append(i)
    return returnList