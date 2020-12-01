def fizzbuzz(n: int):
    """
    >>> fizzbuzz(30)
    'FizzBuzz'
    >>> fizzbuzz(10)
    'Buzz'
    >>> fizzbuzz(27)
    'Fizz'
    """
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
