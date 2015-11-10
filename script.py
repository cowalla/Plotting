from matrix import *
import matplotlib.pyplot as plt

values = []

# Vertical indices
maximum = 100
# Horizontal indices 
sz = 100


def _make_alphas(a, size):
    return [a for i in range(0, size)]


for index in range(0, maximum + 1):
    alpha = float(index)/float(maximum)
    alpha_list = _make_alphas(alpha, sz)
    eigenvalues = matrix_eigenvalues(0, alpha, sz)

    values.append((eigenvalues, alpha_list))

plt.figure()
for eigenvalues, alphas in values:
    plt.plot(eigenvalues, alphas, '.', color='r', markersize=1.8)

plt.axis([-4.5, 4.5, 0, 1])
plt.show()