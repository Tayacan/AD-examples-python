class MatrixError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return self.value

class Matrix:
    def __init__(self,lst):
        """lst is a list rows, eg [[1,2,3],[4,5,6]] for a 2x3 matrix"""
        if not all(map(len,lst)) or len(lst) < 1:
            raise MatrixError("Badly formed matrix")

        self._matrix = lst
        self.rows = len(lst)
        self.columns = len(lst[0])

    def __str__(self):
        s = "["
        for row in self._matrix[:-1]:
            s += "["
            for e in row[:-1]:
                s += str(e) + ", "
            s += str(row[-1]) + "]\n "

        s += "["
        for e in self._matrix[-1][:-1]:
            s += str(e) + ", "
        s += str(self._matrix[-1][-1]) + "]]"

        return s

    def __repr__(self):
        return str(self)

    def __mul__(self,other):
        if self.columns != other.rows:
            raise MatrixError("Incompatible dimensions")

        m = [[0]*other.columns for x in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    m[i][j] = m[i][j] + self._matrix[i][k] * other._matrix[k][j]

        return Matrix(m)

