# -*- coding: utf-8 -*-

# Bottom-up fibonacci
# Laver en liste af alle fibonacci-tal fra
# 0 til n, og returnerer så det nte.
def fib(n):
    if n < 2: return n

    prev,curr = 0,1
    new = -1
    for i in range (2,n+1):
        new = prev + curr
        prev = curr
        curr = new
    return new

# memoized fibonacci
# Decoratoren Memoize gemmer en dictionary over gamle kald, og slår
# op i den frem for at kalde funktionen. Kan bruges på ca. alle funktioner.
def memoize(f,*args):
    d = {}
    def func(*args):
        if args in d:
            return d[args]
        d[args] = f(*args)
        return d[args]
    return func

# Memoize anvendt på fibonacci.
@memoize
def mem_fib(n):
    if n <= 1:
        return n
    return mem_fib(n-1) + mem_fib(n-2)

# Memoize anvendt på fakultetsfunktionen
@memoize
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
