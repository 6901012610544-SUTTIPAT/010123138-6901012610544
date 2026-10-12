class Matrix:
    def __init__(self, data):
        """
        Initialize the matrix with a 2D list of numbers.
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def show(self):
        """
        Display the matrix row by row with aligned formatting.
        """
        for row in self.data:
            print("[ " + "  ".join(f"{val:>4}" for val in row) + " ]")
        print()

    def add(self, other):
        """
        Add another matrix of the same dimensions element-wise.
        """
        #Validate that dimensions match
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to perform addition.")

        result = [
            [self.data[r][c] + other.data[r][c] for c in range(self.cols)]
            for r in range(self.rows)
        ]
        return Matrix(result)

    def subtract(self, other):
        """
        Subtract another matrix of the same dimensions element-wise.
        """
        #Validate that dimensions match
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to perform subtraction.")

        result = [
            [self.data[r][c] - other.data[r][c] for c in range(self.cols)]
            for r in range(self.rows)
        ]
        return Matrix(result)

    def multiplication(self, other):
        """
        Multiply this matrix by another matrix using standard matrix multiplication.
        Requirement: Number of columns in Matrix A must equal number of rows in Matrix B.
        """
        #Validate matrix multiplication condition
        if self.cols != other.rows:
            raise ValueError(
                f"Cannot multiply: Columns of first matrix ({self.cols}) "
                f"must match rows of second matrix ({other.rows})."
            )

        #Result size: (rows of A) x (columns of B)
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)


# ==========================================================
# Demonstration & Testing
# ==========================================================
if __name__ == "__main__":
    #Define test matrices
    m1 = Matrix([
        [1, 2, 3],
        [4, 5, 6]
    ])

    m2 = Matrix([
        [7, 8, 9],
        [1, 2, 3]
    ])

    m3 = Matrix([
        [1, 2],
        [3, 4],
        [5, 6]
    ])

    print("Matrix 1:")
    m1.show()

    print("Matrix 2:")
    m2.show()

    #1. Addition
    print("Matrix 1 + Matrix 2 (add):")
    sum_result = m1.add(m2)
    sum_result.show()

    #2. Subtraction
    print("Matrix 1 - Matrix 2 (subtract):")
    sub_result = m1.subtract(m2)
    sub_result.show()

    #3. Multiplication (2x3 multiplied by 3x2 yields a 2x2 matrix)
    print("Matrix 3:")
    m3.show()

    print("Matrix 1 * Matrix 3 (multiplication):")
    mult_result = m1.multiplication(m3)
    mult_result.show()