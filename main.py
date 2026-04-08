from eigen_module import compute_eigen

def main():
    # Dummy matrix (replace later)
    A = [
        [1, 2],
        [3, 4]
    ]

    print("Input Matrix:")
    print(A)

    # Call your module
    values, vectors = compute_eigen(A)

    print("\nEigenvalues:")
    print(values)

    print("\nEigenvectors:")
    print(vectors)


if __name__ == "__main__":
    main()