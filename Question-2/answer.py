"""
Project Euler question # 2

"""

___author___ = "Marcos Lopez"


from question import *

def fib(n):
    """
    Subsequent number is the sum of previous two.
    This gets heavier as the numbers get larger
    Using the formula Fn = F(n-2)+F(n-1)
    """
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


sum = 0
for n in map(fib, range(0, 4000000)):
    sum += n

print "The answer is %s" % answer
