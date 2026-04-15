import numpy as np

def compute_eigen(A):
    """
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
