    
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
    
    
x = [0, 2, 5, 7]
y = [2, 6, 8, 10]

x = np.array(x)
y = np.array(y)

f = interpolate.interp1d(x, y)

xnew = np.arange(min(x), max(x), 0.1)
ynew = f(xnew)   # use interpolation function returned by `interp1d`
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()

