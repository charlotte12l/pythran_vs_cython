import numpy as np


# pythran export _kendall_dis(int[:], int[:])
def _kendall_dis(x, y):
    sup = 1 + np.max(y)
    arr = np.zeros(sup + ((sup - 1) >> 14), dtype=np.intp)
    i = 0
    k = 0
    size = x.size
    dis = 0


    while i < size:
        while k < size and x[i] == x[k]:
            dis += i
            idx = y[k]
            while idx != 0:
                dis -= arr[idx + (idx >> 14)]
                idx = idx & (idx - 1)

            k += 1

        while i < k:
            idx = y[i]
            while idx < sup:
                arr[idx + (idx >> 14)] += 1
                idx += idx & -idx
            i += 1

    return dis