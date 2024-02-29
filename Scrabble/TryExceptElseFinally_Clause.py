# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:56:43 2023

@author: j_edr
"""

def raise_2nd_exception():
    try:
        pass
        # raise IndexError  # will be a handled exception
        # raise ZeroDivisionError  # unhandled exception
    except IndexError:
        pass
        # raise Exception("Exception in except IE")
    else:
        pass
        # raise Exception("Exception in else")
    finally:
        print("***### Finally ###***")
        print("then it will reraise unhandled or 2nd exception unless there is")
        print("an exception in the finally clause\n")
        # raise Exception("See what happens if there is an exception in finally")