# Solves the first two test cases but not the third.
# I looked at the analysis for the third test case (but not for the first or second) which is why I
# did not revise this to work for the third.

import math

def sieve(n):
    bound = 1 + 2 * math.floor((n - 1) / 2)
    nums = [True for _ in range(3, bound + 1, 2)]
    i = 0
    while (True):
        k = 3
        x = 2 * (i + 1) + 1
        if (x * x > bound): break
        while (True):
            y = k * x
            if (y > bound): break
            nums[((y - 1)//2) - 1] = False
            k += 2
        i += 1
    return [2] + [2 * (i + 1) + 1 for i in range(len(nums)) if nums[i]]

primes = sieve(10 ** 5)
N = len(primes)

num_cases = int(input())
for i in range(1, num_cases + 1):
    Z = int(input())
    last_product = None
    for j in range(N - 1):
        product = primes[j] * primes[j + 1]
        if (product > Z): break
        last_product = product
    print("Case #" + str(i) + ": " + str(last_product))