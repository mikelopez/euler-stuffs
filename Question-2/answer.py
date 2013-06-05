"""
Project Euler question # 2

"""

___author___ = "Marcos Lopez"


import sys
sys.path.append('../')

import timer as _timer
from question import *
from itertools import takewhile


# Start the timer
now = _timer.timer()

# Solution
def gen_fib():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0+f1
                
limit = 4000000
fibs = takewhile(lambda x: x <= limit, gen_fib())
answer = sum(f for f in fibs if f % 2 == 0)


# Print the answer
_timer.print_answer(now, answer)