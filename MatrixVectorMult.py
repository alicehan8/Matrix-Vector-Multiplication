import numpy as np

def innerProduct(a,b):
    """
    Takes two vectors a and b, of equal length, and returns their inner product
    """
    a = a.astype(float)
    b = b.astype(float)
    c = a * b
    x = 0
    for i in range(len(c)):
        x += c[i]
    return x

def AxIP(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    row, col = np.shape(A)
    b = np.zeros(row)
    for i in range(row):
        a = A[i, :]
        b[i] = innerProduct(a,x)
    return b
        

def AxVS(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    row, col = np.shape(A)
    b = np.zeros(row)
    for i in range(col):
        b += x[i] * A[:, i]
    return b

