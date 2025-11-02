def compare_images(X, Y, threshold=5):
    """
    Compare two black-and-white images (2D int arrays of 0s and 1s)
    using a dynamic programming approach to find minimal difference per row.

    Parameters:
        X: list[list[int]] - initial image of size I x J
        Y: list[list[int]] - final image of size I x K
        threshold: int - acceptable difference level

    Returns:
        str: "The images are similar" or "The images are different"
    """

    I = min(len(X), len(Y))  # Number of rows to compare
    total_diff = 0           # Accumulate row differences

    for i in range(I):  # Loop through rows
        J = len(X[i])
        K = len(Y[i])

        # Initialize DP matrix
        D = [[0] * (K + 1) for _ in range(J + 1)]

        # Base cases
        for j in range(J + 1):
            D[j][0] = j
        for k in range(K + 1):
            D[0][k] = k

        # Dynamic programming computation
        for j in range(1, J + 1):
            for k in range(1, K + 1):
                if X[i][j - 1] == Y[i][k - 1]:
                    line1 = D[j - 1][k - 1]
                else:
                    line1 = D[j - 1][k - 1] + 1

                line2 = D[j - 1][k] + 1
                line3 = D[j][k - 1] + 1

                D[j][k] = min(line1, line2, line3)

        row_diff = D[J][K]
        total_diff += row_diff
        print(f"Row {i+1} difference: {row_diff}")

    # Decide image similarity based on total difference
    if total_diff <= threshold:
        print(f"\nTotal difference = {total_diff}")
        return "The images are similar"
    else:
        print(f"\nTotal difference = {total_diff}")
        return "The images are different"


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    X = [
        [1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0],
        [1, 1, 0, 1, 0]
    ]

    Y = [
        [1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1]
    ]

    result = compare_images(X, Y, threshold=4)
    print("\nResult:", result)
