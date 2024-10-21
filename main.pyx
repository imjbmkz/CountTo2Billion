def count_to_billion_py():
    n = 0
    for _ in range(2_000_000_000):
        n += 1
    print(n)

def count_to_billion_cy():
    cdef int n, i
    n = 0
    for i in range(2_000_000_000):
        n += 1
    print(n)