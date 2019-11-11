#!/usr/bin/env python3

import scipy
import matplotlib.pyplot as plt
import numpy as np

# Read from a hardcoded filename
f = scipy.fromfile(open("fm_IQ.dat"), dtype=scipy.complex64)
print("Number of complex items  =", len(f))
print("First and last of the samples:")
print(f)

# Trim the data down and look at the first N points
f = f[0:500]
X = [x.real for x in f]
Y = [x.imag for x in f]
plt.scatter(X,Y, color='red')
#plt.plot(f)
plt.show()
