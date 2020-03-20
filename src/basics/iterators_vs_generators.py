
class MyRange:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        return MyRangeIterator(self)

class MyRangeIterator:
    ''' Iterator for class MyRange'''
    def __init__(self,rangeObj):
        self._rangeObj = rangeObj
        self._pos = self._rangeObj._start

    def __next__(self):
         if self._pos < self._rangeObj._end:
             result = self._pos
             self._pos += 1
             return result
         else:
            raise StopIteration
        

if __name__ == '__main__':
    myrange = MyRange(10, 20)
    for elem in myrange:
        print(elem)