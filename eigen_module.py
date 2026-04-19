import numpy as np

def compute_eigen(A):
    A = np.array(A)

    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")

    values, vectors = np.linalg.eig(A)

    # Sort descending
    idx = values.argsort()[::-1]
    values = values[idx]
    vectors = vectors[:, idx]

    return values, vectors