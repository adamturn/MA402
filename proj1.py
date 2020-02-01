# MA 402
# Project 1
# adam note:	generally the methods will produce results inline with,
#		our project. However, in some cases modifications will
#		need to be made to the return type for certain analysis.
#		Specifically, when I calculated stats for the spectral
#		radii, I returned 'spec_rad' alongside 'fig.show()', etc.
#		You can uncomment function calls to see those plots too.

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
		self.norm2 = np.linalg.norm(self.data, ord=2)
		self.condition = self.norm2 * np.linalg.norm(np.linalg.inv(self.data), ord=2)

	def plt_pattern(self, depth, type):
		evs_real = [np.real(x) for x in self.eigenvals]
		evs_imag = [np.imag(x) for x in self.eigenvals]
		evs_radius = [(np.real(x)**2 + np.imag(x)**2)**0.5 for x in self.eigenvals]
		evs_norm = [self.norm2]
		spec_rad = [self.spectral_radius]
		cond_num = [self.condition]

		for i in range(depth - 1):
			temp_matrix = mxm_matrix(m=self.m)
			evs_real += list(np.real(temp_matrix.eigenvals))
			evs_imag += list(np.imag(temp_matrix.eigenvals))
			evs_radius += list((np.real(temp_matrix.eigenvals)**2 + np.imag(temp_matrix.eigenvals)**2)**0.5)
			spec_rad += [temp_matrix.spectral_radius]
			evs_norm += [temp_matrix.norm2]
			cond_num += [temp_matrix.condition]

		if type == 'evs':
			fig = px.scatter(
				data_frame=None, 
				x=evs_real, 
				y=evs_imag,
				range_x=[-1.5, 1.5],
				range_y=[-1.5, 1.5],
				width=600,
				height=600,
				title='Eigenvalues of {} {}x{} matrices in the Complex Plane'.format(depth, self.m, self.m),
				labels={'x': 'Real Part', 'y': 'Imaginary Part'}
				)
			fig.update_traces(marker=dict(size=2))
			return fig.show()

		if type == 'spec_rad':
			fig = px.histogram(
				data_frame=None,
				x=evs_radius,
				range_x=[0, 1.2],
				title='Moduli of Eigenvalues from {} random {}x{} matrices'.format(depth, self.m, self.m),
				labels={'x': 'Modulus of Eigenvalue'}
				)
			return fig.show()

		if type == 'spectral':
			fig = px.scatter(
				data_frame=None,
				x=[x for x in range(len(spec_rad))],
				y=spec_rad,
				range_y=[0.8, 1.3],
				title='Spectral Radii of {} random {}x{} matrices'.format(depth, self.m, self.m),
				labels={'x': 'ID of random {}x{} matrix'.format(self.m, self.m),
						'y': 'Spectral Radius'
						}
				)
			return fig.show()

		if type == 'norm2':
			fig = px.scatter(
				data_frame=None,
				y=evs_norm,
				x=[x for x in range(len(evs_norm))],
				range_y=[1.5, 2.5],
				title='Behavior of the 2norm of {} random {}x{} matrices'.format(depth, self.m, self.m),
				labels={'y': '2norm', 'x': 'ID of random {}x{} matrix'.format(self.m, self.m)}
				)
			return fig.show()

		if type == 'condition':
			fig = px.histogram(
				data_frame=None,
				x=cond_num,
				title='Behavior of the Condition Number of {} random {}x{} matrices'.format(depth, self.m, self.m),
				labels={'x': 'Condition Number'}
				)
			return fig.show()

		if type== 'condition_scatter':
			fig = px.scatter(
				data_frame=None,
				x=[x for x in range(len(cond_num))],
				y=cond_num,
				title='Behavior of the Condition Number of {} random {}x{} matrices'.format(depth, self.m, self.m),
				labels={'x': 'ID of random {}x{} matrix'.format(self.m, self.m),
						'y': 'Condition Number'
						}
				)
			return fig.show()


# 3.1
"""
Illustrate through well chosen plots what the eigenvals look like.
What is the pattern?
"""
# The general pattern of the eigenvalues is similar to that of the 
# unit circle in the complex plane.

matrixA = mxm_matrix(m=2**5) # 32
matrixB = mxm_matrix(m=2**6) # 64

#matrixA.plt_pattern(depth=500, type='evs')
#matrixB.plt_pattern(depth=1000, type='evs')

# 3.2
"""
What can you say about the limiting behavior of the spectral
radius as m approaches infinity?
"""
matrixC = mxm_matrix(m=2**7) # 128 
matrixD = mxm_matrix(m=2**8) # 256 
#matrixE = mxm_matrix(m=2**15) # 1,048,576  # rip my ram

A_results = matrixA.plt_pattern(depth=1000, type='spectral')
B_results = matrixB.plt_pattern(depth=1000, type='spectral')
#matrixC.plt_pattern(depth=1000, type='spectral')
C_results = matrixD.plt_pattern(depth=1000, type='spectral')
# get the mean and std dev of the spectral radii for m=32,64,256
results_list = [A_results, B_results, C_results]
for result in results_list:
	average = np.mean(result)
	med = np.median(result)
	stdev = np.std(result)
	print("Mean: {} \nMedian: {} \nStd.Dev.: {} \n\n".format(average, med, stdev))

# 3.3
"""
What about the behavior of the 2-norm of such matrices?
What happens as m approaches infinity?
Can you relate this to Problem 1?
"""
matrixA.plt_pattern(depth=1000, type='norm2')
matrixB.plt_pattern(depth=1000, type='norm2')
matrixC.plt_pattern(depth=1000, type='norm2')
matrixD.plt_pattern(depth=1000, type='norm2')

# 3.4
"""
Same question for the condition number.
"""
matrixA.plt_pattern(depth=1000, type='condition_scatter')
matrixB.plt_pattern(depth=1000, type='condition_scatter')
matrixC.plt_pattern(depth=100, type='condition')
matrixD.plt_pattern(depth=100, type='condition')
