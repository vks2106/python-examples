A = [1,2,3,5]


def range_lookup(A):
    return []

def sum_series(A):
    N = len(A) + 1
    return (N**2 + N)//2 - sum(A)

sum_series(A)