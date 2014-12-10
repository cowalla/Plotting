from matrix import *
import matplotlib.pyplot as plt

matrices = []
maximum = 150
sz = 150
for index in range(0, maximum + 1):
    alpha = float(index)/float(maximum)
    matrices.append(PerturbedMatrix(g=0.1, a=float(alpha), size=sz))

plt.figure()
for mat in matrices:
    plt.plot(mat.eigenvalues, mat.alphas, '.')

plt.axis([-4.5, 4.5, 0, 1])
plt.show()


# plt.plot(a.eigenvalues, a.alphas, '.')
# plt.ylabel('some numbers')
# plt.show()