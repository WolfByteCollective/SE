def NumOperations(a,b):
    sum = a + b
    diff = a-b
    product = a*b
    div = a/b
    return [sum, diff, product, div]

print(NumOperations(5,1))