import numpy as np

def reconstruct_image(A, eigenvectors_k):
    """
    Reconstruct image using top-k eigenvectors
    """
    return A @ eigenvectors_k @ eigenvectors_k.T


def compute_error(A, A_k):
    """
    Compute reconstruction error (Frobenius norm)
    """
    return np.linalg.norm(A - A_k)


def run_reconstruction(A, eigenvectors, k_values):
    """
    Run reconstruction for multiple k values
    """
    reconstructed_images = []
    errors = []

    for k in k_values:
        V_k = eigenvectors[:, :k]

        A_k = reconstruct_image(A, V_k)
        err = compute_error(A, A_k)

        reconstructed_images.append(A_k)
        errors.append(err)

    return reconstructed_images, errors