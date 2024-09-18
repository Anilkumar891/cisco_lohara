def is_odd(N):
    return  N%2==1


def is_even(N):
    return N%2==0

import math
def is_prime(N):
    N_sqrt=int(math.sqrt(N))
    for i in range(2,N_sqrt+1):
        if N%i==0:
            return False
    return True
