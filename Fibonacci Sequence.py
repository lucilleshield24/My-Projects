def fibseq(n):
    firstterm = 1
    secondterm = 1
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        for x in range(2, n):
            a = firstterm + secondterm
            firstterm = secondterm
            secondterm = a
        print(a)

# x * x-1 * x-2 * x-3 * ... * 1
def factorial(x):
    total = 1
    for n in range(1, x+1):
        total = total * n
    return total

def recursivefactorial(x):
    total = 1
    if x > 1:
        total = x * recursivefactorial(x-1)
    return total
