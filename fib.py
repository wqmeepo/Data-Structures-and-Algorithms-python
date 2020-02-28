def fib(max):
    n, a, b = 0, 0, 1
    l = []
    while n < max:
        l.append(b)
        a, b = b, a + b
        n += 1
    return l


if __name__ == '__main__':
    for i in range(10):
        print(fib(i))