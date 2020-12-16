import math


def euler1(max_value):
    return sum(x for x in range(max_value) if (x % 3 == 0 or x % 5 == 0))


def euler2(max_value):
    return sum(x for x in fibonacci(max_value) if (x % 2 == 0 and x < max_value))


# TODO E3: What is the largest prime factor of the number 600851475143
def euler3(n):
    for i in reversed(range(3, n, 2)):
        if is_odd(i):
            if is_factor(i, n):
                if is_prime(i):
                    # print("xxx " + str(i))
                    return i
    return "no prime factor found"


def fibonacci(max_value):
    fibs = [1, 2]
    while True:
        f1 = fibs[len(fibs) - 1]
        f2 = fibs[len(fibs) - 2]
        n = f1 + f2
        if n <= max_value:
            fibs.append(n)
        else:
            break
    return fibs


def is_factor(i, n):
    return n % i == 0


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def is_prime(n):
    # corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # divisible by 2 or 3, not prime
    if n % 2 == 0 or n % 3 == 0:
        return False

    # 6k±1 discovery
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def is_prime_factor(i, n):
    return is_prime(i) and is_factor(i, n)


def test_is_prime():
    assert is_prime(0) == False
    print("is_prime(0) = " + str(is_prime(0)))
    assert is_prime(2) == True
    print("is_prime(2) = " + str(is_prime(2)))
    assert is_prime(4) == False
    print("is_prime(4) = " + str(is_prime(4)))
    assert is_prime(7) == True
    print("is_prime(7) = " + str(is_prime(7)))
    assert is_prime(22) == False
    print("is_prime(22) = " + str(is_prime(22)))
    assert is_prime(23) == True
    print("is_prime(23) = " + str(is_prime(23)))


def test_is_factor():
    i = 1
    n = 2
    assert is_factor(i, n) == True
    print("factors(1, 2) = " + str(is_factor(i, n)))
    assert is_prime_factor(i, n) == False
    print("prime_factors(1, 2) = " + str(is_prime_factor(i, n)))
    i = 4
    n = 9
    assert is_factor(i, n) == False
    print("factors(4, 9) = " + str(is_factor(i, n)))
    assert is_prime_factor(i, n) == False
    print("prime_factors(4, 9) = " + str(is_prime_factor(i, n)))
    i = 5
    n = 10
    assert is_factor(i, n) == True
    print("factors(5, 10) = " + str(is_factor(i, n)))
    assert is_prime_factor(i, n) == True
    print("prime_factors(5, 10) = " + str(is_prime_factor(i, n)))


def test_fibonacci():
    assert fibonacci(25) == [1, 2, 3, 5, 8, 13, 21]
    print("Fibonacci(25) = " + str(fibonacci(25)))


if __name__ == '__main__':
    # Fundamental tests
    print("#####  Unit Tests:  #####")
    test_is_prime()
    test_is_factor()
    test_fibonacci()

    # maxPrimeFactors(573891))  # 191297


    # Euler tests
    print("")
    print("#####  Euler Tests:  #####")

    assert euler1(1000) == 233168
    print("Euler1(1000) = " + str(euler1(1000)))

    assert euler2(4000000) == 4613732
    print("Euler2(4000000) = " + str(euler2(4000000)))

    assert euler3(5143) == 139
    print("Euler3(5143) = " + str(euler3(5143)))
    # TODO complete/correct the E3 assertion/algorithm
    # assert euler3(514391) ==
    print("Euler3(514391) = " + str(euler3(514391)))
    # assert euler3(64745143) ==
    print("Euler3(64745143) = " + str(euler3(64745143)))
    # assert euler3(600851475143) ==
    # print("Euler3(600851475143) = " + str(euler3(600851475143)))
