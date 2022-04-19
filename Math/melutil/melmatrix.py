class Matrix:
    def __init__(self, rows, cols, initial_value=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[initial_value for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, item):
        return self.matrix[item]

    def __mul__(self, other):
        pass # fixa skalär mul

    def __matmul__(self, other):
        result = Matrix(self.rows, other.cols)

    @staticmethod
    def get_identity_matrix(size):
        matrix = Matrix(size, size)
        for i in range(size):
            matrix[i][i] = 1
        return matrix



print(Matrix(2, 3))
print(Matrix.get_identity_matrix(5))