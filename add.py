

def add(x,y):
    sum = x + y
    return sum

def addNum(sum,sums):
    sums.insert(0, sum)
    if len(sums) > 10:
        sums.pop(-1)
    return sums


