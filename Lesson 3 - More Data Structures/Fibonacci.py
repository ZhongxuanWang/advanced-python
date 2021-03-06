# Fibonacci Implementation in different ways

# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...

import time


def timing(func):  # You just learnt it in the last lesson.. This is a decorator!
    def wrapper(*args, **kwargs):
        old = time.time()
        ret = func(*args, **kwargs)
        print(f'{func.__name__}{args} took {(time.time() - old) * 1000} ms')
        return ret

    return wrapper


@timing
def plain_rec(n):
    if n <= 3:
        return 1
    else:
        return plain_rec(n - 1) + plain_rec(n - 2)


@timing
def dp_memoization(n):
    if n <= 3:
        return 1
    if dp_list[n - 1] is not None:
        first = dp_list[n - 1]
    else:
        first = dp_memoization(n - 1)

    if dp_list[n - 2] is not None:
        second = dp_list[n - 2]
    else:
        second = dp_memoization(n - 2)

    dp_list[n] = first + second
    return dp_list[n]


@timing
def dp_tabulation(n):
    for i in range(4, n+1):
        dp_list[i-1] = dp_list[i-2] + dp_list[i-3]
    return dp_list[n-1]


if __name__ == '__main__':
    # See the printing!! Function with the same parameter is being called multiple times, which could be optimized.
    # Also, function with greater depth takes less time since they have fewer recursions.

    NthFibToRun = 7  # ADJUST YOUR INPUT HERE. Eg. 7 means the 7th number, NOT index 7 (which becomes the 8th number).

    a = time.time()
    print(plain_rec(NthFibToRun))
    rec_cost = (time.time() - a) * 1000
    print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    a = time.time()
    dp_list = [None] * (NthFibToRun+1)
    print(dp_memoization(NthFibToRun))
    print(f'Total time cost for DP with Memoization\t is: {(time.time() - a) * 1000} ms')
    dp_list = [None] * (NthFibToRun+1)
    dp_list[0] = 0
    dp_list[1] = 1
    dp_list[2] = 1
    a = time.time()
    print(dp_tabulation(NthFibToRun))
    print(f'Total time cost for DP with Tabulation\t is: {(time.time() - a) * 1000} ms')
    print(f'Total time cost for Plain Recursion \t is: {rec_cost} ms')
