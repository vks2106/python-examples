def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]


def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

print(PowTwoGen(3))

if __name__ == '__main__':
    pass
