def is prime(n):
    if n < 2:
        return false
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_peimes(start, end):
    try:
        start, end = int(start), int(end)
        if start > end:
            start, end = end, start
            primes_sum = sum(num for num in range(start, end + 1) if is _primes(num))
