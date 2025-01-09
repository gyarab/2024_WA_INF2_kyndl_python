import string

def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def is_prime(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(a,b):
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers.")
    if a > b:
        a, b = b, a
    if a == b:
        return []
    return [x for x in range(a, b + 1) if is_prime(x)] 

def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    return [text[i:i+3] for i in range(0, len(text), 3)]

def caesar_encode(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    if any(char not in string.ascii_letters for char in text):
        raise ValueError("Input must contain only English alphabet letters.")
    return "".join([chr(ord(x) + 3) for x in text])

    

def caesar_decode(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    if any(char not in string.ascii_letters for char in text):
        raise ValueError("Input must contain only English alphabet letters.")
    return "".join([chr(ord(x) - 3) for x in text])


    if __name__ == "__main__":
        print(fibonacci(250))
        print(is_prime(97))
        print(primes_in_range(1, 50))
        print(split_into_threes("abcdefgh"))
        print(caesar_encode("Zebra"))
        print(caesar_decode("Bohemians"))
