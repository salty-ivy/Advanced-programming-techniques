'''
type is a metaclass built in, 
A meta class is a class of classes that controls the creation process and other behavior of those classe

type is one such class 
type can also create classes dynamically
'''

#dynamic class creation via type

class Demo:
    pass

DemoClassVar = type('Demo',(),{})
print(DemoClassVar)


## paranthesis can help in inheting from a class, curly braces can help in 
## passing attributes.

## all built in classes like list, tuple, str, int, etc are class made by type 
# metaclass, thus inheriting from them.


####  creating a custom metaclass is by inheriting type class and using
#### metaclass keyword and telling the class to use that metaclass for its creation process and other behavior controls

class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubClass(MyClass):
    pass

print(type(MyMeta))
print(type(MyClass))
print(type(MySubClass))


## __new__ vs __init__

'''
__new__ is used when one wants to define dict or bases tuples before the class is created. The return value of __new__is usually an instance of cls. __new__ allows subclasses of immutable types to customize instance creation. It can be overridden in custom metaclasses to customize class creation. __init__ is usually called after the object has been created so as to initialize it.

'''

'''
__call__ is magic method called when obj is called as function 
'''



'''

The expression Foo() creates a new instance of class Foo. When the interpreter encounters Foo(), the following occurs:

The __call__() method of Foo’s parent class is called. Since Foo is a standard new-style class, its parent class is the type metaclass, so type’s __call__() method is invoked.

That __call__() method in turn invokes the following:

__new__()
__init__()

'''





