## The singleton design pattern is useful when you need to create only one object or you need some sort of object capable of maintaining a global state for your program.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(cls)
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]

class Demo(metaclass=SingletonMeta):
    pass

obj1 = Demo()
obj2 = Demo()

print(Demo() is Demo())


