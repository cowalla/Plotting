import numpy
from numpy import exp, zeros, pi, cos


class PerturbedMatrix(object):
    def __init__(self, g, a, size):
        super(PerturbedMatrix, self).__init__()
        self.matrix = self.construct_matrix(g, a, size)
        self.eigenvalues = self._eigenvalues()
        self.alphas = [a for i in range(0, size)]

    def construct_matrix(self, g, a, size):
        _matrix = zeros(shape=(size, size))
        matrix_norm = (2 * pi * a)
        minus_computed = exp(-g)
        plus_computed = exp(g)

        for i in range(0, size):
            minus, plus = _construct_indeces(i, size)
            _matrix[i, minus] = minus_computed
            _matrix[i, i] = 2*cos(matrix_norm*i)
            _matrix[i, plus] = plus_computed

        return _matrix

    def _eigenvalues(self):
        return numpy.linalg.eigvals(self.matrix)


def _construct_indeces(index, size):
    if index == 0:
        return size - 1, 1
    if index == size - 1:
        return index - 1, 0

    return index - 1, index + 1