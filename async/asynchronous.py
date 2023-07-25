import asyncio
import time

# start = time.time()
# print("hello")
# for _ in range(5):
#     print("hi")
# print("finished")
# end = time.time()
# print(end-start)

# print("#########################################")


async def main():
    print("hello")
    # await foo('hi')
    task = asyncio.create_task(foo('hi'))
    # await task
    print('finished')

async def foo(text):
    for _ in range(5):
        print(text)
    # await asyncio.sleep(3)
start = time.time()
asyncio.run(main())
end = time.time()

print(end-start)