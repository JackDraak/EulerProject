def euler1(max_value):
    return sum(x for x in range(max_value) if (x % 3 == 0 or x % 5 == 0))


def euler2(max_value):
    return sum(x for x in fibonacci(max_value) if (x % 2 == 0 and x < max_value))


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


def is_factor(integer):
    if integer[1] % integer[0] == 0:
        return True
    else:
        return False


def is_prime(integer):
    if integer <= 1:
        return False
    test = 2
    while True:
        if test == integer:
            return True
        elif integer % test == 0:
            break
        else:
            test += 1
    return False  # i.e. 'elif' was affirmative; break out of loop asap.


def is_prime_factor(n):
    return is_prime(n[0]) and is_factor([n[0], n[1]])


if __name__ == '__main__':
    # Fundamental tests
    assert is_prime(0) == False
    assert is_prime(2) == True

    factors = [1, 2]
    assert is_factor(factors) == True
    print("factors 1, 2 " + str(is_factor(factors)))
    assert is_prime_factor(factors) == False
    print("prime_factors 1, 2 " + str(is_prime_factor(factors)))
    factors = [4, 9]
    assert is_factor(factors) == False
    print("factors 4, 9 " + str(is_factor(factors)))
    assert is_prime_factor(factors) == False
    print("prime_factors 4, 9 " + str(is_prime_factor(factors)))
    factors = [5, 10]
    assert is_factor(factors) == True
    print("factors 5, 10 " + str(is_factor(factors)))
    assert is_prime_factor(factors) == True
    print("prime_factors 5, 10 " + str(is_prime_factor(factors)))

    # Euler tests
    assert euler1(1000) == 233168
    print("Euler 1: 1000 = " + str(euler1(1000)))

    assert euler2(4000000) == 4613732
    print("Euler 2: 4000000 = " + str(euler2(4000000)))

    # random tests
    # for i in range(50):
    #     if is_prime(i):
    #         print('is_prime(' + str(i) + ') ')
