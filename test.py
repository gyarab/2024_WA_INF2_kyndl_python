def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    if __name__ == "__main__":
        print(fibonacci(250))

def is_prime(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

    if __name__ == "__main__":
        print(is_prime(97))

print(fibonacci(255))
print(is_prime(5))