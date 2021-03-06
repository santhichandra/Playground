# Factorial of a positive integer

def fact(n):
    return n if n in [0, 1] else n * fact(n - 1)

# Factorial of a positive integer with lambda function

factL = lambda x: x if x in [0, 1] else x * factL (x - 1)

# Fibanocci number

def fib(n):
    return n if n in [0, 1] else fib(n - 1) + fib(n - 2)

# Fibanocci number with lambda function

fibL = lambda x: x if x in [0, 1] else fibL(x - 2) + fibL(x - 1)

# Square root of a positive integer

def mysqrt(n, lb=1.0):
    rb = n / lb
    if (rb < lb):
        lb, rb = rb, lb
    return lb if ((rb - lb) < 0.000001) else mysqrt(n, (lb+rb)/2.0)

# Euclid's Algorithm to find the GCD/HCF of two positive integers

def gcd(x, y):
   return x if (y == 0) else gcd(y, x % y)

# Euclid's Algorithm to find the GCD/HCF of two positive integers with lambda function

gcdL = lambda x, y: x if (y == 0) else gcdL(y, x % y)

if __name__ == "__main__":
  print (fact(8))
  print (factL(8))
  print (fib(8))
  print (fibL(8))
  print (mysqrt(1234))
  print (gcd(30, 50))
  print (gcdL(30, 50))
