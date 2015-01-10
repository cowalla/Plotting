from matrix import *
import matplotlib.pyplot as plt

matrices = []
maximum = 250
sz = 250

for index in range(0, maximum + 1):
    alpha = float(index)/float(maximum)
    matrices.append(PerturbedMatrix(g=0.0, a=float(alpha), size=sz))

plt.figure()
for mat in matrices:
    plt.plot(mat.eigenvalues, mat.alphas, '.', color='r', markersize=1.8)

plt.axis([-4.5, 4.5, 0, 1])
plt.show()