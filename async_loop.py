import asyncio
import time
async def count(i):
    for _ in range(10):
        pass
    await asyncio.sleep(1)
    print("ended",i)

async def main():
    for i in range(10):
        task = asyncio.create_task(count(i))
    await task
start = time.time()
asyncio.run(main())
end = time.time()
print(end-start)

# async def count2(i):
#     for _ in range(10):
#         pass
#     await asyncio.sleep(1)
#     print("ended",i)

# async def sync():
#     for i in range(10):
#         await count2(i)
# start = time.time()
# asyncio.run(sync())
# end = time.time()
# print(end-start)