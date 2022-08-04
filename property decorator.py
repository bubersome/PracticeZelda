from datetime import datetime

class Generic:
    def __init__(self):
        self._x = 10 

    def getter(self):
        print('get x xxx')
        print(datetime.now())
        return self._x

    def setter(self, value):
        print('set x')
        self._x = value

    # def getter(self):
    #     pass

    def deleter(self):
        print('delete x')
        del self._x

    x = property(getter, setter, deleter)

generic = Generic()
generic.x = 4
print(generic.x)


