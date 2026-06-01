# main.py

import sys
import os
# Get the current directory
current_dir = os.path.dirname(__file__)
# Add the parent directory to the Python module search path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
print(parent_dir)


from MyApp import functions as fun , greet
# # import functions
# from MyApp.functions import a
# from MyApp.functions import *
print(fun.a)
# power=functions.power(3,2)
# print(power)
# # Now you can use functions from the functions module

# greet.SayHellow("Akash")
# avg=functions.average(4,8)
# print(avg)

# print(functions.sum(12,34))
