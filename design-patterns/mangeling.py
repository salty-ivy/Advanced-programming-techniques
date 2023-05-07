class A:
    def __init__(self, name):
        self.__name = name

obj = A()
print(obj.__name) # not allowed standard behavior

# could make things really confusing when working with meta classes.
obj.__name = "hello world" # dynamically creates new public attribute __name and works.
