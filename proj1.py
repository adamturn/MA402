# MA 402
# Project 1
# Adam Turner

# Problem 3
"""
Consider random mxm matrices whose entries are independent samples
of the normal distribution with mean zero and standard deviation
m**(-1/2), i.e., sampled from N(0, m**(-1/2)).
"""
import numpy as np
import plotly.express as px


class mxm_matrix:
    def __init__(self, m=np.random.randint(1, 10)):
        self.m = m
        self.data = np.random.normal(0, self.m**(-1/2), (self.m, self.m))
        self.eigenvals = np.linalg.eig(self.data)[0]
        self.spectral_radius = max(np.absolute(self.eigenvals))


# 3.1
"""
Illustrate through well chosen plots what the eigenvals look like.
What is the pattern?
"""
matrixA = mxm_matrix(m=2**5)
matrixB = mxm_matrix(m=2**6)
matrixC = mxm_matrix(m=2**10)
matrixD = mxm_matrix(m=2**15)


def plt_evpattern(matrix, depth):
	evs_real = [np.real(x) for x in matrix.eigenvals]
	evs_imag = [np.imag(x) for x in matrix.eigenvals]

	for i in range(depth - 1):
		temp_mat = mxm_matrix(m=matrix.m)
		evs_real += list(np.real(temp_mat.eigenvals))
		evs_imag += list(np.imag(temp_mat.eigenvals))

	fig = px.scatter(
		data_frame=None, 
		x=evs_real, 
		y=evs_imag,
		width=600,
		height=600
		)

	return fig.show()


plt_evpattern(matrixA, 1000)
plt_evpattern(matrixB, 1000)
plt_evpattern(matrixC, 1000)
plt_evpattern(matrixD, 1000)
