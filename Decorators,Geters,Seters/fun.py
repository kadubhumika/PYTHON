from functools import reduce
numbers = [1,2,4,5]
def sum(a,b):
    return a+b

new = reduce(sum,numbers)
print(new)