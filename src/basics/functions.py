def f_bad():
    if 2<4:
    	return True
    else:
    	return False

def f_good():
    return 2<4

def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

print(is_leap(2000))

if __name__ == '__main__':
    pass