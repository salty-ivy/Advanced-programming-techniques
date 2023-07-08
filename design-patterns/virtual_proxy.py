"""
A virtual proxy, which uses lazy initialization to defer the creation of a computationally expensive object until the moment it is actually needed
"""


class LazyProperty:
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print(f"function overriden: {self.method}")
        print(f"function's name: {self.method_name}")

    def __get__(self, obj, cls):
        print(obj)
        if not obj:
            return None
        value = self.method(obj) # obj as self.
        print(f'value {value}')

        setattr(obj, self.method_name, value)  # now setting the actual actual value to that method name. ( for no execution next time. )
        print("value---->", value)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print(f'initializing self._resource which is: {self._resource}')
        self._resource = tuple(range(5))
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # do more work...
    print(t.resource)
    print(t.resource)


if __name__ == "__main__":
    main()
