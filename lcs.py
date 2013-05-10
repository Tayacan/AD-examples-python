def lcs(a,b):
    if (len(a) == 0) or (len(b) == 0):
        return []

    if a[-1] == b[-1]:
        return lcs(a[:-1],b[:-1]) + [a[-1]]

    lcs_a = lcs(a,b[:-1])
    lcs_b = lcs(a[:-1],b)

    return max(lcs_a,lcs_b,key=len)
