"""

Project Euler Question # 1

"""
import sys
sys.path.append('../')
import timer as _timer
from question import *

# Start the timer
now = _timer.timer()

# The solution
total = sum([x for x in range(1000) if x%3==0 or x%5==0])

# print the answer
_timer.print_answer(now, total)




