def memory_test():
    a = [1] * (10 ** 8)
    b = [2] * (2 * 10 ** 8)
    del a
    return b[0]
