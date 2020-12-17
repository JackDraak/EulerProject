# Euler1: The sum of integers in a range [1000] that are divisible by 3 or 5
def euler1(max_value):
    return sum(x for x in range(max_value) if (x % 3 == 0 or x % 5 == 0))


# Euler2: The sum of even Fibonacci numbers [less than 4,000,000]
def euler2(max_value):
    return sum(x for x in fibonacci(max_value) if (x % 2 == 0 and x < max_value))


# Euler3: The largest prime factor [of the number 600851475143 (UNTESTED value)]
# This is a brute-force approach. There is a better way, but this should work, given time.
def euler3(n):
    for i in reversed(range(3, int(n / 2), 2)):
        if is_small(i):
            continue
        if is_prime_factor(i, n):
            return i
    return "no prime factor found"


# Euler4: The largest palindrome made from the product of two n-digit numbers [3].
def euler4(n):
    if n > 10:
        return "I don't think you want to wait for me to process an answer that large"
    if n < 2:
        return None

    i_max = 10**n                   # i.e. 100, 1000, 10000...
    i_min = i_max - (10**(n - 1))   # i.e. 90, 900, 9000...
    test_set = range(i_min, i_max)  # i.e. [90-99]. [900-999], [9000-9999]...
    max_palindrome = 0

    for x in test_set:
        for y in test_set:
            test_integer = x * y
            if is_palindrome(test_integer) and test_integer > max_palindrome:
                max_palindrome = test_integer

    if max_palindrome > 0:
        return max_palindrome
    return "end of line"


def is_palindrome(n):
    if type(n) != int:
        return "extend function to check strings"
    size = len(str(n))
    if size <= 1:
        return False
    for i in range(0, int(size/2)):
        f = str(n)
        if int(f[i]) != int(f[size - i - 1]):
            return False
    return True


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


def is_small(n):  # i.e divisible by 3 or 5
    return n % 3 == 0 or n % 5 == 0


def is_prime(n):  # optimized prime qualifier
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


def test_is_prime(debug):
    assert is_prime(0) == False
    if debug:
        print("is_prime(0) = " + str(is_prime(0)))
    assert is_prime(2) == True
    if debug:
        print("is_prime(2) = " + str(is_prime(2)))
    assert is_prime(4) == False
    if debug:
        print("is_prime(4) = " + str(is_prime(4)))
    assert is_prime(7) == True
    if debug:
        print("is_prime(7) = " + str(is_prime(7)))
    assert is_prime(22) == False
    if debug:
        print("is_prime(22) = " + str(is_prime(22)))
    assert is_prime(23) == True
    if debug:
        print("is_prime(23) = " + str(is_prime(23)))

    for i in range(-1, 255):
        if debug:
            print("is_prime(" + str(i) + ") = " + str(is_prime(i)))


def test_is_factor(debug):
    i = 1
    n = 2
    assert is_factor(i, n) == True
    if debug:
        print("factors(1, 2) = " + str(is_factor(i, n)))
    assert is_prime_factor(i, n) == False
    if debug:
        print("prime_factors(1, 2) = " + str(is_prime_factor(i, n)))
    i = 4
    n = 9
    assert is_factor(i, n) == False
    if debug:
        print("factors(4, 9) = " + str(is_factor(i, n)))
    assert is_prime_factor(i, n) == False
    if debug:
        print("prime_factors(4, 9) = " + str(is_prime_factor(i, n)))
    i = 5
    n = 10
    assert is_factor(i, n) == True
    if debug:
        print("factors(5, 10) = " + str(is_factor(i, n)))
    assert is_prime_factor(i, n) == True
    if debug:
        print("prime_factors(5, 10) = " + str(is_prime_factor(i, n)))


def test_fibonacci(debug):
    assert fibonacci(25) == [1, 2, 3, 5, 8, 13, 21]
    if debug:
        print("Fibonacci(25) = " + str(fibonacci(25)))


def test_eulers(debug):
    if debug:
        print("")
    if debug:
        print("#####  Euler Tests:  #####")
    if debug:
        print("")

    assert euler1(1000) == 233168
    if debug:
        print("Euler1(1000) = " + str(euler1(1000)))
    if debug:
        print("")

    assert euler2(4000000) == 4613732
    if debug:
        print("Euler2(4000000) = " + str(euler2(4000000)))
    if debug:
        print("")

    assert euler3(5143) == 139
    if debug:
        print("Euler3(5143) = " + str(euler3(5143)))

    assert euler3(14391) == 41
    if debug:
        print("Euler3(14391) = " + str(euler3(14391)))
    if debug:
        print("")

    # these work, but take a couple seconds, so are commented-out
    # assert euler3(4745143) == 97
    # print("Euler3(4745143) = " + str(euler3(4745143)))

    # UNTESTED: I assume this will work, but...
    # assert euler3(600851475143) == 6857
    # print("Euler3(600851475143) = " + str(euler3(600851475143)))
    # print("")

    assert euler4(2) == 9009
    if debug:
        print("Euler4(2) = " + str(euler4(2)))

    assert euler4(3) == 906609
    if debug:
        print("Euler4(3) = " + str(euler4(3)))

    assert euler4(4) == 99000099
    if debug:
        print("Euler4(4) = " + str(euler4(4)))


def test_is_palindrome(debug):
    assert is_palindrome(1201) == False
    if debug:
        print("is_palindrome(1201) = " + str(is_palindrome(1201)))
    assert is_palindrome(906609) == True
    if debug:
        print("is_palindrome(906609) = " + str(is_palindrome(906609)))
    assert is_palindrome(101) == True
    if debug:
        print("is_palindrome(101) = " + str(is_palindrome(101)))
    assert is_palindrome(11) == True
    if debug:
        print("is_palindrome(11) = " + str(is_palindrome(11)))
    assert is_palindrome(1660661) == True
    if debug:
        print("is_palindrome(1660661) = " + str(is_palindrome(1660661)))
    assert is_palindrome(9) == False
    if debug:
        print("is_palindrome(9) = " + str(is_palindrome(9)))
    assert is_palindrome(2112) == True
    if debug:
        print("is_palindrome(2112) = " + str(is_palindrome(2112)))
    assert is_palindrome(21999912) == True
    if debug:
        print("is_palindrome(21999912) = " + str(is_palindrome(21999912)))
    assert is_palindrome(12) == False
    if debug:
        print("is_palindrome(12) = " + str(is_palindrome(12)))
    assert is_palindrome("abc") == "extend function to check strings"
    if debug:
        print("is_palindrome('abc') = " + str(is_palindrome("abc")))


if __name__ == '__main__':
    # Unit tests (bool: False = silent)
    test_is_prime(False)
    test_is_factor(False)
    test_fibonacci(False)
    test_is_palindrome(False)

    # Euler tests (bool: False = silent)
    test_eulers(True)

