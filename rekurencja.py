from functools import cache


# ciag fibbonaciego [1,1,2,3,5,8 ...]


def fibi(n):
    a = b = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    # end for
    return a


# end def


def fib_r(n):
    if n < 3:
        return 1
    else:
        return fib_r(n - 1) + fib_r(n - 2)
    # end if


# end def


for i in range(1, 50):
    print(i, fibi(i))

# w tym przypadku rekurencja znacznie pogarsza rozwiazanie
