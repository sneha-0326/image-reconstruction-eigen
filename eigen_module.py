import numpy as np

def compute_eigen(A):
    """
<<<<<<< HEAD
    Compute eigenvalues and eigenvectors of A^T A
    """

    # Step 1: Compute A^T A
    ATA = np.dot(A.T, A)

    # Step 2: Use eigh (better for symmetric matrices)
    eigenvalues, eigenvectors = np.linalg.eigh(ATA)

    return eigenvalues, eigenvectors


def sort_eigen(eigenvalues, eigenvectors):
    """
    Sort eigenvalues in descending order and rearrange eigenvectors
    """

    idx = np.argsort(eigenvalues)[::-1]

    sorted_eigenvalues = eigenvalues[idx]
    sorted_eigenvectors = eigenvectors[:, idx]

    return sorted_eigenvalues, sorted_eigenvectors


def select_top_k(eigenvalues, eigenvectors, k):
    """
    Select top k eigenvalues and eigenvectors
    """

    k = min(k, eigenvectors.shape[1])  # safety check

    top_k_values = eigenvalues[:k]
    top_k_vectors = eigenvectors[:, :k]

    return top_k_values, top_k_vectors


def project_data(A, eigenvectors_k):
    """
    Project original data onto top-k eigenvectors
    """

    return np.dot(A, eigenvectors_k)
=======
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
>>>>>>> eigen-module
