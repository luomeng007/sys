# -*- coding: utf-8 -*-
"""
Created on Tue Nov  10 16:49:12 2020

@author: 15025

first case:
    the computer will print one result one second
second case:

"""

import sys
import time

# first case: one element appear at one second
# for i in range(10):
#     print(i)
#     time.sleep(1)


# second case
for i in range(10):
    print(i, end=" ")
    time.sleep(1)


# third case: one element appear at one second
# for i in range(10):
#     print(i, end=" ")
#     sys.stdout.flush()
#     time.sleep(1)


# last case, same as third case: one element appear at one second
# for i in range(10):
#     print(i, end=' ', flush=True)
#     time.sleep(1)
