def function(key, value=0):
    """Return a dictionary and a list..."""
    d = {key: value}
    l = [key, value]
    return d, l

#print(function(3))


a = 1
if isinstance(a, int):
    print('a is an integer.')
else:
    print('a is not an integer.')

def is_instance(a,int):
    return isinstance(a,int)

if __name__ == '__main__':
    pass