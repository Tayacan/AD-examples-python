from fib import memoize
import random

# comment out the @memoize decorator to see the difference it makes.
@memoize
def lcs(a,b):
    if (len(a) == 0) or (len(b) == 0):
        return []

    if a[-1] == b[-1]:
        return lcs(a[:-1],b[:-1]) + [a[-1]]

    lcs_a = lcs(a,b[:-1])
    lcs_b = lcs(a[:-1],b)

    return max(lcs_a,lcs_b,key=len)

# lcs of two randomly generated strings of 0's and 1's, each of length 100.
#print ''.join(lcs(''.join([random.choice('10') for x in range(100)]),''.join([random.choice('10') for x in range(100)])))

# Test of the LPS(S) == LCS(S,S') theory
c = 0
for i in range(10000):
    s = ''.join([random.choice('abcdefghijklmnopqrstuvxyz') for x in range(random.randrange(10,20))])
    p = lcs(s,s[::-1])
    if p != p[::-1]:
        c += 1

print c
