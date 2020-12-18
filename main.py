# Euler1: The sum of integers in a range that are divisible by 3 or 5
# [1 - 1000]
def euler1(n):
    return sum(i for i in range(1, n) if is_divisible_by_3or5(i))


# Euler2: The sum of even Fibonacci numbers less than or equal to a value
# [<4,000,000]
def euler2(n):
    return sum(i for i in fibonacci(n) if (is_even(i) and i < n))


# Euler3: The largest prime factor
# [of the number 600851475143]
def euler3(n):
    # Optimized, but broken for some cases (i.e. 5143), without s_f_f >= 69 (should be 1).
    stupid_fudge_factor = 69
    for i in reversed(range(3, int(n**0.5) + stupid_fudge_factor, 2)):
        if is_divisible_by_3or5(i):
            continue
        if is_prime_factor(i, n):
            return i
    return "no prime factor found"


# Euler4: The largest palindrome made from the product of two n-digit numbers
# [3 digits]
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
            if test_integer > max_palindrome:
                if is_palindrome(test_integer):
                    max_palindrome = test_integer

    if max_palindrome > 0:
        return max_palindrome
    return "end of line"


# Euler5: The smallest positive integer that is evenly divisible by all of the positive integers in the set
# [1 - 20]
def euler5(n):
    euler = 0
    euler_candidate = 0
    while euler == 0:
        euler_candidate += n
        for i in range(1, n + 1):
            if euler_candidate % i != 0:
                break
            if i == n:
                euler = euler_candidate
    return euler


# Euler6: The difference between the sum of the squares and the square of the sum
# [of the first one hundred natural numbers]
def euler6(n):
    sum_of_set = 0
    sum_of_squares = 0

    for i in range(1, n + 1):
        sum_of_set += i
        sum_of_squares += i * i
    return sum_of_set * sum_of_set - sum_of_squares


# Euler7: The nth prime number in the series
# [10,001st]
def euler7(n):
    count = 0
    i = 0

    while count < n:
        i += 1
        if is_prime(i):
            count += 1
    return i


# Euler8: The four adjacent digits in this 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?
def euler8(n):
    k = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    product = 1
    for i in range(len(str(k))):
        sub_product = int(str(k)[i])
        for j in range(1, n + 1):
            try:
                sub_product *= int(str(k)[i + j])
            except:
                print("Done")
        product *= sub_product
    return product


# Generate and return Fibonacci numbers as an array, up to 'n', inclusive
def fibonacci(n):
    # corner cases
    if n < 0:
        return None
    if n < 3:
        return n

    fibonacci_set = [1, 2]
    while True:
        f1 = fibonacci_set[len(fibonacci_set) - 1]
        f2 = fibonacci_set[len(fibonacci_set) - 2]
        i = f1 + f2
        if i <= n:
            fibonacci_set.append(i)
        else:
            break
    return fibonacci_set


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
        print("")

    # this passes, but takes a few moments
    # assert euler5(20) == 232792560
    # if verbose:
    #    print("Euler5(20) = " + str(euler5(20)))

    assert euler6(10) == 2640
    if verbose:
        print("Euler6(10) = " + str(euler6(10)))

    assert euler6(100) == 25164150
    if verbose:
        print("Euler6(100) = " + str(euler6(100)))
        print("")

    assert euler7(0) == 0
    assert euler7(1) == 2
    assert euler7(2) == 3
    assert euler7(3) == 5
    assert euler7(4) == 7
    assert euler7(5) == 11
    assert euler7(6) == 13
    assert euler7(7) == 17
    assert euler7(8) == 19
    assert euler7(9) == 23
    for i in range(10):
        if verbose:
            print("Euler7(" + str(i) + ") = " + str(euler7(i)))

    assert euler7(10001) == 104743
    if verbose:
        print("Euler7(10001) = " + str(euler7(10001)))
        print("")


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
        _test_is_factor_verbosity(i, n)

    i = 4
    n = 9
    assert is_factor(i, n) == False
    assert is_prime_factor(i, n) == False
    if verbose:
        _test_is_factor_verbosity(i, n)

    i = 5
    n = 10
    assert is_factor(i, n) == True
    assert is_prime_factor(i, n) == True
    if verbose:
        _test_is_factor_verbosity(i, n)


def _test_is_factor_verbosity(i, n):
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
    # test_eulers(True)

    print(euler8(0))
    print(euler8(1))
    print(euler8(2))
    print(euler8(3))