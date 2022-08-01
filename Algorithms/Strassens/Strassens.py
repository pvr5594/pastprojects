import numpy as np


def strassens(A, B):
    """
    Uses Strassen’s method for matrix multiplication to return the product of the two
    provided Matrices A and B.
    :param A: the first matrix to multiply. Implemented as a np.array
    :param B: The second matrix to multiply. Implemented as a np.array
    :return: The product of A and B
    """
    a = np.array(A)
    b = np.array(B)
    if len(a) == 1:
        return a * b

    n = a.shape[0] // 2
    a0 = a[:n, :n]  # UPPER LEFT
    a1 = a[:n, n:]  # UPPER RIGHT
    a2 = a[n:, :n]  # LOWER LEFT
    a3 = a[n:, n:]  # LOWER RIGHT

    b0 = b[:n, :n]  # UPPER LEFT
    b1 = b[:n, n:]  # UPPER RIGHT
    b2 = b[n:, :n]  # LOWER LEFT
    b3 = b[n:, n:]  # LOWER RIGHT

    p = strassens((a0 + a3), (b0 + b3))
    q = strassens((a2 + a3), b0)
    r = strassens(a0, (b1 - b3))
    s = strassens(a3, (b2 - b0))
    t = strassens((a0 + a1), b3)
    u = strassens((a2 - a0), (b0 + b1))
    v = strassens((a1 - a3), (b2 + b3))

    c0 = p + s - t + v
    c1 = r + t
    c2 = q + s
    c3 = p - q + r + u

    top = np.hstack((c0, c1))
    bottom = np.hstack((c2, c3))

    return np.vstack((top, bottom))


def basic_smoke_test():
    smoke1 = [[1, 2], [3, 4]]
    smoke2 = [[5, 6], [7, 8]]
    result = strassens(smoke1, smoke2)
    expected = np.array([[19, 22], [43, 50]])
    assert (np.array_equal(result, expected))
    print("First test passed")

    smoke3 = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 11, 12, 13]]
    result = strassens(smoke3, smoke3)
    expected = np.array([[70, 80, 90, 100], [136, 158, 180, 202], [202, 236, 270, 304], [268, 314, 360, 406]])
    assert (np.array_equal(result, expected))
    print("Second test passed")


if __name__ == "__main__":
    basic_smoke_test()
