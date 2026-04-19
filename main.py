from preprocessing import load_image
from eigen_module import compute_eigen


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


if __name__ == "__main__":
    main()