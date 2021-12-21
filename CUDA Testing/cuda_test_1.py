import numpy as np 
import numba 
from numba import cuda 
from numba import jit


from timeit import default_timer as timer

# To run on CPU
def func(a, n):
    for i in range(n):
        a[i]+= 1

# To run on GPU
@numba.jit 
def func2(x):
    return x+1

if __name__=="__main__":

    n = 10

    for x in range(1,8):

        n = 10**x

        a = np.ones(n, dtype = np.float64)

        print("\nn count = ",n)

        start_cpu = timer()
        func(a,n)
        print("without GPU:", timer()-start_cpu)

        start_gpu = timer()
        func2(a)
        cuda.profile_stop()
        print("with GPU:", timer()-start_gpu)

        diff = ((-start_cpu+start_gpu)/start_cpu)*100
        print("cpu/gpu %",diff)