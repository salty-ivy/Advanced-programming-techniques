from dataclasses import dataclass
from functools import partial


power_of_2 =  partial(pow,2)

print(power_of_2(6))



class CommonBase:
    pass

class Base1(CommonBase):
    pass

class Base2(CommonBase):
    pass

class MyClass(Base1,Base2):
    pass


instance_of = MyClass()

print(MyClass.__mro__)



#######  descriptors

### visible in class attributes assignment

class RevealAccess(object):
    def __init__(self,initval=None,name="var"):
        self.val = initval
        self.name = name

    def __get__(self,obj,owner):
        print("retrieving..")
        return self.val

    def __set__(self,obj,val):
        print("updating")
        self.val = val

    def __delete__(self,obj):
        print("deleting")

x=RevealAccess(10,"test")
print(x)
print(x.val)


class MyClass(object):
    x = RevealAccess(100,"var 'x' ")
    y = 4



## encapsulation

class UserAccount:
    def __init__(self,username,password):
        self._username = username
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,val):
        self._password = val



### operator overloading , polymorphism , dundur methods

class Matrix(object):
    def __init__(self,rows :list):
        if len(set(len(row) for row in rows))>1:
            raise ValueError("Matrix rows must be of same length")
        self.rows = rows

    ### operator overloading for +

    def __add__(self,other):
        ## isinstance is used to simulate function overloading
        if not isinstance(other,Matrix):
            print("unknown operand.")
        if(
                len(self.rows) != len(other.rows) or 
                len(self.rows[0]) != len(other.rows[0])
          ):
            raise ValueError("Matrix dimensions did not match")
        else:
            return Matrix([
                        [a+b for a,b in zip(a_row,b_row)]
                        for a_row,b_row in zip(self.rows,other.rows)
                    ])

    def __sub__(self,other):
        if(
                len(self.rows) != len(other.rows) or
                len(self.rows[0]) != len(other.rows[0])
                ):
            raise ValueError("Matrix dimensions did not match")
        else:
            return Matrix([
                [a-b for a,b in zip(a_row,b_row)]
                for a_row,b_row in zip(self.rows,other.rows)
            ])

    def __mul__(self,other):
        pass


# generators with yield -> pause the function and return an intermediate result and saves the contect for continuation..

def fibonacci():
    a,b=0,1

    while True:
        yield b #return b and pause , save the context
        a,b = b,a+b

## now you cam retrieve new values from gen like they are iterators  with next function

fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))




### dataclass decorators with immutable object that comes with __init__ , __repr__, __eq__

@dataclass(frozen=True)
class Vector:
    x: int
    y: int


    def __add__(self,other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self,other):
        return Vector(self.x+other.x, self.y+other.y)

    



m1 =  Matrix([
        [1,2,3],
        [4,5,6],
    ])

m2 = Matrix([
        [1,2,3],
        [1,0,0],
    ])

m3 = m1 + m2

print(m3.rows)


user = UserAccount("aman","testing321")
print(user.password)
user.password = "newpassword"
print(user.password)



obj = MyClass()

print(obj.x)


## enumerations ...



from enum import Enum 

class Days(Enum):
    MONDAY = 0
    TUESDAY = 1















