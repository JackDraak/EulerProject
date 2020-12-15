def euler1(max_value):
    return sum(x for x in range(max_value) if (x % 3 == 0 or x % 5 == 0))


def euler2(max_value):
    return sum(x for x in fibonacci(max_value) if (x % 2 == 0 and x < max_value))


def fibonacci(max_value):
    fibs = [1, 2]
    n = 0
    while True:
        f1 = fibs[len(fibs) - 1]
        f2 = fibs[len(fibs) - 2]
        n = f1 + f2
        if n <= max_value:
            fibs.append(n)
        else:
            break
    return fibs


if __name__ == '__main__':
    # Euler tests
    print("Euler 1: 1000 = " + str(euler1(1000)))
    print("Euler 2: 4000000 = " + str(euler2(4000000)))

    # random tests
    print("Fibonacci numbers up to 6000000, inclusive = " + str(fibonacci(6000000)))
    even_fibs = []
    for fib_number in fibonacci(6000000):
        if fib_number % 2 == 0:
            even_fibs.append(fib_number)
    print("even Fibonacci numbers up to 6000000, inclusive = " + str(even_fibs))
