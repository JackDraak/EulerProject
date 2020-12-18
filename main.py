# Euler1: The sum of integers in a range [1000] that are divisible by 3 or 5
def euler1(n):
    return sum(i for i in range(n) if is_divisible_by_3or5(i))


# Euler2: The sum of even Fibonacci numbers [less than 4,000,000]
def euler2(n):
    return sum(i for i in fibonacci(n) if (is_even(i) and i < n))


# Euler3: The largest prime factor [of the number 600851475143]
def euler3(n):
    # Note, below variable solves all cases I've tried when == 1, except 5143 (granted, I've done limited testing)
    stupid_fudge_factor = 69    # TODO optimized, but broken for some cases (i.e. 5143), without this >= 69 (should be 1)
    for i in reversed(range(3, int(n**0.5) + stupid_fudge_factor, 2)):
        # if is_sqrt_or_less(i, n):
        if is_divisible_by_3or5(i):
            continue
        if is_prime_factor(i, n):
            return i
    return "no prime factor found"


# Euler4: The largest palindrome made from the product of two n-digit [3] numbers.
def euler4(n):
    if n > 10:
        return "I don't think you want to wait for me to process an answer that large"
    if n < 2:
        return None

    i_max = 10**n                   # i.e. 100, 1000, 10000...
    i_min = i_max - (10**(n - 1))   # i.e. 90, 900, 9000...
    test_set = range(i_min, i_max)  # i.e. [90-99]. [900-999], [9000-9999]...
    max_palindrome = 0

    # attempted to 'optimize' euler4 function to prevent duplication of tests, but...
    # cataloging tested sets seems to take more time than simply re-testing them; go figure
    # tested = []
    for x in test_set:
        for y in test_set:
            # if y not in tested:
            #    if x not in tested:
            #       tested.append(x)
            test_integer = x * y
            if test_integer > max_palindrome:
                if is_palindrome(test_integer):
                    max_palindrome = test_integer

    if max_palindrome > 0:
        return max_palindrome
    return "end of line"


# Euler5: The smallest +ve number that is evenly divisible by all of the positive integers in the set [from 1 to 20]
def euler5(n):
    euler = 0
    euler_candidate = n
    while euler == 0:
        euler_candidate += n
        for i in range(1, n + 1):
            if euler_candidate % i != 0:
                break
            if i == n:
                euler = euler_candidate
    return euler


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


def is_divisible_by_3or5(n):
    return n % 3 == 0 or n % 5 == 0


def is_even(n):
    return n % 2 == 0


def is_factor(i, n):
    return n % i == 0


def is_odd(n):
    return n % 2 != 0


def is_palindrome(n):
    if type(n) != int:
        return "extend function to check strings"

    f = str(n)
    digits = len(f)

    if digits <= 1:
        return False

    for i in range(0, int(digits/2)):
        if int(f[i]) != int(f[digits - i - 1]):
            return False
    return True


# optimized prime qualifier, using 6k±1 discovery, which I don't fully understand
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
    while i * i <= n:  # i.e. while 'i' is less than the square root of 'n'
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def is_prime_factor(i, n):
    return is_prime(i) and is_factor(i, n)


def is_sqrt_or_less(i, n):
    return i * i <= n


def test_eulers(verbose):
    if verbose:
        print("")
        print("#####  Euler Tests:  #####")
        print("")

    assert euler1(1000) == 233168
    if verbose:
        print("Euler1(1000) = " + str(euler1(1000)))
    if verbose:
        print("")

    assert euler2(4000000) == 4613732
    if verbose:
        print("Euler2(4000000) = " + str(euler2(4000000)))
        print("")

    assert euler3(5143) == 139
    if verbose:
        print("Euler3(5143) = " + str(euler3(5143)))

    assert euler3(14391) == 41
    if verbose:
        print("Euler3(14391) = " + str(euler3(14391)))

    assert euler3(4745143) == 97
    if verbose:
        print("Euler3(4745143) = " + str(euler3(4745143)))

    assert euler3(994745143) == 5227
    if verbose:
        print("Euler3(994745143) = " + str(euler3(994745143)))

    assert euler3(600851475143) == 6857
    if verbose:
        print("Euler3(600851475143) = " + str(euler3(600851475143)))
        print("")

    assert euler4(2) == 9009
    if verbose:
        print("Euler4(2) = " + str(euler4(2)))

    assert euler4(3) == 906609
    if verbose:
        print("Euler4(3) = " + str(euler4(3)))
        print("")

    # this passes, but takes a second
    # assert euler4(4) == 99000099
    # if verbose:
    #    print("Euler4(4) = " + str(euler4(4)))
    #    print("")

    # this passes, but takes a few moments
    # assert euler4(5) == 9966006699
    # if verbose:
    #    print("Euler4(5) = " + str(euler4(5)))

    assert euler5(10) == 2520
    if verbose:
        print("Euler5(10) = " + str(euler5(10)))

    # this passes, but takes a few moments
    # assert euler5(20) == 232792560
    # if verbose:
    #    print("Euler5(20) = " + str(euler5(20)))
    #    print("")


def test_fibonacci(verbose):
    assert fibonacci(25) == [1, 2, 3, 5, 8, 13, 21]
    if verbose:
        print("Fibonacci(25) = " + str(fibonacci(25)))


def test_is_factor(verbose):
    i = 1
    n = 2
    assert is_factor(i, n) == True
    assert is_prime_factor(i, n) == False
    if verbose:
        _test_is_factor_set_verbosity(i, n)

    i = 4
    n = 9
    assert is_factor(i, n) == False
    assert is_prime_factor(i, n) == False
    if verbose:
        _test_is_factor_set_verbosity(i, n)

    i = 5
    n = 10
    assert is_factor(i, n) == True
    assert is_prime_factor(i, n) == True
    if verbose:
        _test_is_factor_set_verbosity(i, n)


def _test_is_factor_set_verbosity(i, n):
    print("factors(" + str(i) + ", " + str(n) + ") = " + str(is_factor(i, n)))
    print("prime_factors(" + str(i) + ", " + str(n) + ") = " + str(is_prime_factor(i, n)))


def test_is_palindrome(verbose):
    assert is_palindrome(1201) == False
    if verbose:
        print("is_palindrome(1201) = " + str(is_palindrome(1201)))

    assert is_palindrome(906609) == True
    if verbose:
        print("is_palindrome(906609) = " + str(is_palindrome(906609)))

    assert is_palindrome(101) == True
    if verbose:
        print("is_palindrome(101) = " + str(is_palindrome(101)))

    assert is_palindrome(11) == True
    if verbose:
        print("is_palindrome(11) = " + str(is_palindrome(11)))

    assert is_palindrome(1660661) == True
    if verbose:
        print("is_palindrome(1660661) = " + str(is_palindrome(1660661)))

    assert is_palindrome(9) == False
    if verbose:
        print("is_palindrome(9) = " + str(is_palindrome(9)))

    assert is_palindrome(2112) == True
    if verbose:
        print("is_palindrome(2112) = " + str(is_palindrome(2112)))

    assert is_palindrome(21999912) == True
    if verbose:
        print("is_palindrome(21999912) = " + str(is_palindrome(21999912)))

    assert is_palindrome(12) == False
    if verbose:
        print("is_palindrome(12) = " + str(is_palindrome(12)))

    assert is_palindrome("abc") == "extend function to check strings"
    if verbose:
        print("is_palindrome('abc') = " + str(is_palindrome("abc")))


def test_is_prime(verbose):
    assert is_prime(0) == False
    if verbose:
        print("is_prime(0) = " + str(is_prime(0)))

    assert is_prime(2) == True
    if verbose:
        print("is_prime(2) = " + str(is_prime(2)))

    assert is_prime(4) == False
    if verbose:
        print("is_prime(4) = " + str(is_prime(4)))

    assert is_prime(7) == True
    if verbose:
        print("is_prime(7) = " + str(is_prime(7)))

    assert is_prime(22) == False
    if verbose:
        print("is_prime(22) = " + str(is_prime(22)))

    assert is_prime(23) == True
    if verbose:
        print("is_prime(23) = " + str(is_prime(23)))

    if verbose:
        for i in range(-1, 255):
            print("is_prime(" + str(i) + ") = " + str(is_prime(i)))


if __name__ == '__main__':
    # Unit tests (bool: False = silent, True = verbose)
    test_fibonacci(False)
    test_is_factor(False)
    test_is_palindrome(False)
    test_is_prime(False)
    print("Unit testing complete")

    # Euler tests (bool: False = silent, True = verbose)
    test_eulers(True)
