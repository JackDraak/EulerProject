# Euler1: The sum of integers less than 'n' that are divisible by 3 or 5
# [1 - 1000]
def euler1(n):
    return sum(integer for integer in range(1, n) if is_divisible_by_3or5(integer))


# Euler2: The sum of even Fibonacci numbers less than the value of 'n'
# [<4,000,000]
def euler2(n):
    return sum(this_fibonacci for this_fibonacci in fibonacci(n) if (is_even(this_fibonacci) and this_fibonacci < n))


# Euler3: The largest prime factor of 'n'
# [600851475143]
def euler3(n):
    # Optimized, but broken for some cases (i.e. n=5143), without s_f_f >= 69 (should be 1).
    stupid_fudge_factor = 69
    for i in reversed(range(3, int(n**0.5) + stupid_fudge_factor, 2)):
        if is_divisible_by_3or5(i):
            continue
        if is_prime_factor(i, n):
            return i
    return None


# Euler4: The largest palindrome made from the product of two n-digit integers
# [3 digits]
def euler4(n):
    if n > 10:
        return "If you want the answer today, maybe try n <= 5"
    if n < 2:
        return None

    i_max = 10**n
    i_min = i_max - (10**(n - 1))
    integer_candidates = range(i_min, i_max)
    max_palindrome = 0

    for x in integer_candidates:
        for y in integer_candidates:
            test_integer = x * y
            if test_integer > max_palindrome:
                if is_palindrome(test_integer):
                    max_palindrome = test_integer

    if max_palindrome > 0:
        return max_palindrome
    else:
        return None


# Euler5: The smallest positive integer that is evenly divisible by all of the positive integers less than 'n'
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


# Euler6: The difference between the sum of the squares, and the square of the sum, of the integers up to 'n', inclusive
# [of the first one hundred natural numbers]
def euler6(n):
    sum_of_set = 0
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_set += i
        sum_of_squares += i * i
    return sum_of_set * sum_of_set - sum_of_squares


# Euler7: The nth (literally) prime number in the series
# [10,001st]
def euler7(n):
    count = 0
    i = 0
    while count < n:
        i += 1
        if is_prime(i):
            count += 1
    return i


# Euler8: The frame of 'n' sequential digits in this 1000-digit number that have the greatest product
# [13 digit frames]
def euler8(n):
    if n <= 0:
        return 0
    k = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    accumulator = 0
    for frame_begin in range(len(str(k))):
        this_frame = []
        for digit in range(0, n):
            # try:except is more performant when a rare occurrence, so I'm sticking
            # with this rather than checking if the index is in-bounds every cycle
            try:
                this_frame.append(int(str(k)[frame_begin + digit]))
            except IndexError:
                continue

        if this_frame.__contains__(0):
            continue

        else:
            product = int(this_frame[0])
            for c in range(1, len(this_frame)):
                product *= this_frame[c]

        if product > accumulator:
            accumulator = product
    if accumulator == 0:
        return "(n = " + str(n) + ") is too large, no frames that size have a product > 0"
    return accumulator


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


def test_eulers():
    print("")
    print("Euler Test\t(Test Value)\t\t\tTest Result")
    print("----- ----\t----- ------\t\t\t---- ------")

    assert euler1(1000) == 233168
    print("Euler1\t\t(1000)\t\t\t=\t\t" + str(euler1(1000)))

    assert euler2(4000000) == 4613732
    print("Euler2\t\t(4000000)\t\t=\t\t" + str(euler2(4000000)))

    assert euler3(5143) == 139
    assert euler3(14391) == 41
    assert euler3(4745143) == 97
    assert euler3(994745143) == 5227
    assert euler3(600851475143) == 6857
    print("Euler3\t\t(600851475143)\t=\t\t" + str(euler3(600851475143)))

    assert euler4(3) == 906609
    assert euler4(2) == 9009
    print("Euler4\t\t(3)\t\t\t\t=\t\t" + str(euler4(3)))

    assert euler5(10) == 2520
    print("Euler5\t\t(20)\t\t\t=\t\t" + str(euler5(20)))

    assert euler6(10) == 2640
    assert euler6(100) == 25164150
    print("Euler6\t\t(100)\t\t\t=\t\t" + str(euler6(100)))

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
    assert euler7(10001) == 104743
    print("Euler7\t\t(10001)\t\t\t=\t\t" + str(euler7(10001)))

    assert euler8(0) == 0
    assert euler8(1) == 9
    assert euler8(2) == 81
    assert euler8(3) == 648
    assert euler8(4) == 5832
    assert euler8(5) == 40824
    assert euler8(6) == 285768
    assert euler8(7) == 2571912
    assert euler8(8) == 7838208
    assert euler8(13) == 23514624000
    print("Euler8\t\t(13)\t\t\t=\t\t" + str(euler8(13)))


def test_fibonacci():
    assert fibonacci(25) == [1, 2, 3, 5, 8, 13, 21]
    return True


def test_is_factor():
    i = 1
    n = 2
    assert is_factor(i, n) == True
    assert is_prime_factor(i, n) == False
    i = 4
    n = 9
    assert is_factor(i, n) == False
    assert is_prime_factor(i, n) == False
    i = 5
    n = 10
    assert is_factor(i, n) == True
    assert is_prime_factor(i, n) == True
    return True


def test_is_palindrome():
    assert is_palindrome(1201) == False
    assert is_palindrome(906609) == True
    assert is_palindrome(101) == True
    assert is_palindrome(11) == True
    assert is_palindrome(1660661) == True
    assert is_palindrome(9) == False
    assert is_palindrome(2112) == True
    assert is_palindrome(21999912) == True
    assert is_palindrome(12) == False
    assert is_palindrome("abc") == "extend function to check strings"
    return True


def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(7) == True
    assert is_prime(22) == False
    assert is_prime(23) == True
    return True


def batched_unit_tests():
    print("Unit testing:", end=" ")
    if test_fibonacci():
        print("pass fibonacci", end=", ")
    if test_is_factor():
        print("pass is_factor", end=", ")
    if test_is_palindrome():
        print("pass is_palindrome", end=", ")
    if test_is_prime():
        print("pass is_prime")


if __name__ == '__main__':
    batched_unit_tests()
    test_eulers()


