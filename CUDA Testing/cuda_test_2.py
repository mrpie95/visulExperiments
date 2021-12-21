import numba
import math
import numpy as np


WIDTH = 1000
HEIGHT = 800

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

SQRT_TWOPI = np.float32(math.sqrt(2 * math.pi))

@numba.vectorize(['float32(float32, float32, float32)'], target='cuda')
def gaussian(x, x0, sigma):
    return math.exp(-((x - x0) / sigma)**2 / 2) / SQRT_TWOPI / sigma


@numba.vectorize(['float32(float32, float32)'], target='cuda')
def test_cuda(data, val):
    return val

@numba.vectorize(['complex128(complex128)'], target='cuda')
def calc_complex(x):
    return complex(RE_START+(x/WIDTH)*(RE_END-RE_START),IM_START+(x/HEIGHT)*(IM_END-IM_START))


np.set_printoptions(threshold=np.inf)

WIDTH = 200
HEIGHT = 200


data = np.zeros((WIDTH,HEIGHT), dtype=np.complex128)

print(data)
print(data[1,1])

o = calc_complex(data)

print(o)

x = np.linspace(-3, 3, 10000, dtype=np.float32)
#print(x)
g = gaussian(x, 0, 1)  # 1D result



x2d = x.reshape((100,100))
g2d = gaussian(x2d, 0, 1) # 2D result