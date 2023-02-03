from typing import Any
from warnings import warn
# function annotations

def name(fname:str, lname: str)->str:
    #walrus operator , assignment operator which evaluates as an expression
    # x = 0 is assigned and evaluated to 0 
    if x:=0:
        print("x=0")
    else:
        print(x)
    if y:=1:
        print("y=1")
        print(y)
    print(name.__annotations__)
    return f"{fname}-{lname}"


# positional only arguments
# arg before / is positional and after * is keyword
def concatinate(first :str, second:str,/,*,delim:str)->str:
    return delim.join([first,second])

def newConcatinate(*items, delim: str)->str:
    return delim.join(items)


# union type annotations 
#use the word Unioin or|
def key_lookup(d: dict[str|bytes, Any ],key :str|bytes )->Any:
    for k,v in d.items():
        if key.lower()==k.lower():
            print("found")
            break
        else:
            print("not found")

## supoose key look up has been updated and the old name was checkkey
def __getattr__(name:str):
    if name=="checkkey":
        print("deprecated")
        warn(f"{name} is deprecated",DeprecationWarning)
        return key_lookup

    raise AttributeError(f"module {__name__} has no attribute {name}")


# pattern matching 

def matchMe(string :str)->bool:
    match (string):
        case("aman"):
            print("pandey")
            return True
        case("pandey"):
            print("aman")
            return True
        case("nothing"):
            print("nothing")
            return True
        case _:
            print("defaut")
            return False


matchMe("aman")
matchMe("pandey")
matchMe("nothing")
matchMe("pytohn3")
key_lookup({"k1":2132_213213_312313,"k2":13123},"k1")
# concatinate("aman","pandey","*")
print(concatinate("aman","pandey",delim="$"))
name("aman", "pandey")


