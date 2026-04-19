import numpy as np

def compute_eigen(A):
    """
    Compute eigenvalues and eigenvectors of A^T A
    """

    # Step 1: Compute A^T A
    ATA = A.T @ A

    # Step 2: Eigen decomposition (since ATA is symmetric)
    eigenvalues, eigenvectors = np.linalg.eigh(ATA)

    # Step 3: Sort in descending order
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    return eigenvalues, eigenvectors


def select_top_k(eigenvalues, eigenvectors, k):
    """
    Select top k eigenvalues and eigenvectors
    """

    k = min(k, eigenvectors.shape[1])  # safety check

    top_k_values = eigenvalues[:k]
    top_k_vectors = eigenvectors[:, :k]

    return top_k_values, top_k_vectors
