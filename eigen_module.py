import numpy as np

def compute_eigen(A):
    """
    Computes eigenvalues and eigenvectors of matrix A

    Parameters:
        A (list or numpy array): Input matrix

    Returns:
        values (numpy array): Eigenvalues
        vectors (numpy array): Eigenvectors
    """

    # Convert to numpy array
    A = np.array(A)

    # Check if matrix is square
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square for eigen decomposition")

    try:
        # Compute eigenvalues and eigenvectors
        values, vectors = np.linalg.eig(A)

        # Sort eigenvalues in descending order
        idx = values.argsort()[::-1]
        values = values[idx]
        vectors = vectors[:, idx]

        return values, vectors

    except Exception as e:
        print("Error in eigen computation:", e)
        return None, None