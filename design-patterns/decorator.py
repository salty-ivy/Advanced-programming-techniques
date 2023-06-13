'''
The decorator pattern shines when used for implementing cross-cutting concerns (j.mp/wikicrosscut). Examples of cross-cutting concerns are as follows:

'''

import functools


def memorize(fn):
    cache = dict()

    @functools.wraps(fn)
    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return wrapper


# using memorization 

sum_cache = {0:0}

@memorize
def number_sum(n):
    assert(n>=0), "n munt be > 0"

    if n == 0:
        return 0
    else:
        #print("call for: ", n, n-1)
        return n + number_sum(n-1)

#number_sum(5)

if __name__=='__main__':
    from timeit import Timer
    t = Timer('number_sum(300)', 'from __main__ import number_sum')
    print('Time:', t.timeit())


