"""
Project Euler question # 2

"""

___author___ = "Marcos Lopez"


from itertools import takewhile
from question import *


def gen_fib():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0+f1
                
limit = 4000000
fibs = takewhile(lambda x: x <= limit, gen_fib())
answer = sum(f for f in fibs if f % 2 == 0)

print "The answer is %s" % answer
