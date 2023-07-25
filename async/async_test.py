import asyncio

class A():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    async def main(self):
        return self.fname+self.lname

obj = A("aman","pandey")
print(asyncio.run(obj.main()))