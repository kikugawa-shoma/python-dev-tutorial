def fizzbuzz(n: int, fizz: int = 3, buzz: int = 5) -> str:
    """
      >>> fizzbuzz(30)
      'FizzBuzz'
      >>> fizzbuzz(10)
      'Buzz'
      >>> fizzbuzz(27)
      'Fizz'
    """

    if n % (fizz*buzz) == 0:
        return "FizzBuzz"
    elif n % fizz == 0:
        return "Fizz"
    elif n % buzz == 0:
        return "Buzz"
    else:
        return str(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    a = 2
    fizzbuzz(a)
