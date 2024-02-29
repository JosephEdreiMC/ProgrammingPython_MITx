# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 17:46:19 2023

@author: j_edr
"""

import numpy as np

def polysum (n,s):
    term_1 = 0.25*n*s**2/np.tan(np.pi/n)
    term_2 = (n*s)**2
    wanted_sum = term_1 + term_2
    # No idea why round did not work on its own.
    result=float('%.4f' % round(wanted_sum, 4))

    return result

    