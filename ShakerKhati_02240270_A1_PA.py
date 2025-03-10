def is prime(n):
    if not isinstance(n, int)or n <= 1:
        return False 
    return all (n % i != 0 fot i in range (2, int(n**0.5) + 1))