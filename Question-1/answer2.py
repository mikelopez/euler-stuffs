"""

Project Euler Question # 1
Attempting a quicker solution than 0.6x ms responses

This one takes 0.8 ms, is indeed slower

"""
import sys
sys.path.append('../')
import timer as _timer
from question import *

# Start the timer
now = _timer.timer()

# The solution
starter = 0
total = 0
while starter < 1000:
    if starter%3 == 0 or starter%5 == 0:
        total += starter
    starter += 1

# print the answer
_timer.print_answer(now, total)



