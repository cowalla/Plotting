from matrix import *
import matplotlib.pyplot as plt

values = []
maximum = 200
sz = 200

class AlphasList(list):
    def __init__(self, alpha, iterable):
        self.alpha = alpha

        super(AlphasList, self).__init__(iterable)

    def __getitem__(self, item):
        """Since all the values are the same, don't actually do the lookup"""
        return self.alpha


def _make_alphas(a, size):
    return [a for i in range(0, size)]


for index in range(0, maximum + 1):
    alpha = float(index)/float(maximum)
    alpha_list = AlphasList(alpha, _make_alphas(alpha, sz))
    eigenvalues = matrix_eigenvalues(0, alpha, sz)

    values.append((eigenvalues, alpha_list))

plt.figure()
for eigenvalues, alphas in values:
    plt.plot(eigenvalues, alphas, '.', color='r', markersize=1.8)

plt.axis([-4.5, 4.5, 0, 1])
plt.show()