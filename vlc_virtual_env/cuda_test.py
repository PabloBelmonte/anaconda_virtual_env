import numpy as np
import time
from timeit import default_timer as timer

from numba import vectorize, cuda


@vectorize(['float32(float32, float32)'], target='cuda')
def VectorAdd(a, b):
    return a + b

# def VectorAdd_slow(a, b, c):
#     for i in range(a.size):
#         c[i] = a[i] + b[i]

def main():
    N = 32000000
    
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.ones(N, dtype=np.float32)
    
    # start = time.time()
    start = timer()
    C = VectorAdd(A, B)
    # VectorAdd_slow(A, B, C)
    vector_add_time = timer() - start
    print ("C[:5] = " + str(C[:5]))
    print ("C[-5:] = " + str(C[-5:]))

    print (f"VectorAdd took for {vector_add_time} seconds")

if __name__=='__main__':
    main()