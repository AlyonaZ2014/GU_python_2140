class Matrix:
    def __init__(self, mtr):
        self.mtr = mtr

    def __str__(self):
        return '\n'.join(map(str, self.mtr))

    def __add__(self, other):
        if len(self.mtr) == len(other.mtr):
            for el in range(len(self.mtr)):
                for i in range(len(other.mtr[el])):
                    self.mtr[el][i] = self.mtr[el][i] + other.mtr[el][i]
            return Matrix.__str__(self)
        else:
            try:
                raise ValueError()
            except ValueError:
                return ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")
            return

m_1 = Matrix([[11,2,3],[4,5,6],[117,8,9]])
print(m_1, end='\n\n')
m_2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
print(m_2, end='\n\n')
print(m_1 + m_2)
