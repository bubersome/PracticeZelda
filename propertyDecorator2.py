from datetime import datetime

class Generic:
    def __init__(self):
        self._x = 10 
    @property
    def x(self):
        print('get x xxx')
        print(datetime.now())
        print(self._x)
        return self._x

    @x.setter
    def x(self, value):
        print('set x')
        self._x = value

    # def getter(self):
    #     pass

    @x.deleter
    def x(self):
        print('delete x')
        del self._x

    # x = property(getter, setter, deleter)

generic = Generic()
generic.x 
generic.x = 4
print(generic.x)


