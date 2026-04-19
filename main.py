from preprocessing import load_image
from eigen_module import compute_eigen
from reconstruction import run_reconstruction

import matplotlib.pyplot as plt


def main():
    # Step 1: Load image → matrix
    A = load_image("test.jpg")

    print("Image matrix shape:", A.shape)

    # Step 2: Compute eigen
    values, vectors = compute_eigen(A)

    print("\nEigenvalues:")
    print(values)

    print("\nEigenvectors shape:")
    print(vectors.shape)

    # -------------------------------
    # 🔥 Person 4 (YOUR PART STARTS)
    # -------------------------------

    k_values = [5, 10, 20, 50, 100]

    images, errors = run_reconstruction(A, vectors, k_values)

    print("\nReconstruction Errors:")
    for k, err in zip(k_values, errors):
        print(f"k = {k} → error = {err:.4f}")

    # Plot graph
    plt.plot(k_values, errors, marker='o')
    plt.xlabel("k (number of eigenvectors)")
    plt.ylabel("Reconstruction Error")
    plt.title("Error vs k")
    plt.show()

    # -------------------------------
    # 🔥 Person 4 ENDS
    # -------------------------------


if __name__ == "__main__":
    main()
