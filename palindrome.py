# -*- coding: utf-8 -*-

import random
from fib import memoize

@memoize
def lps(S):                                                  # T(n)
    i,j = 0,len(S)-1
    if len(S) > 1:
        if S[i] == S[j]:
            return str(S[i]) + lps(S[i+1:j]) + str(S[i])    # c3 + T(n-2)
        else:
            z1 = lps(S[:-1])                                # T(n-1)
            z2 = lps(S[1:])                                 # T(n-1)
            return max(z1,z2,key=len)                       # c2 (vi påstår at len er O(1))
    else:
        return S                                            # c1

#Efficiency test
s = ''.join([random.choice('abcde') for x in range(100)])
print ''.join(lps(s))
