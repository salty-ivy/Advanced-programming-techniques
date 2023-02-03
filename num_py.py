import numpy
import time

li = [x for x in range(10000000)]
arr = numpy.array(li)

sq = []
start = time.time()
for x in li:
    sq.append(x*x)
end = time.time()

print(end-start)

sq = []
start = time.time()
for x in arr:
    sq.append(x*x)
end = time.time()

print(end-start)