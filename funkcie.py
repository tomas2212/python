def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def f():
	for num in range(2,10):
            if num%2 == 0:
                print "Found an even number", num
                continue
            print "Found a number", num

