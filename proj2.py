# -----------
# MA 402: Project #2
# Adam Turner
# -----------
# Goal: Experiments with Monte Carlo integration. Introduction of quasi-random numbers.
# -----------
import random
import pandas as pd
import plotly.express as px

SEED = 11

# Problem 2
#	The infamous RANDU generator was part of the Scientific Subroutine Package on IBM
#	mainframe computers in the 1960's; the generator corresponds to
#		I_n+1 = (a * I_n + c) mod m,	n = 0, 1, ...
#	with a = 65539, c = 0 and m = 2**31.
# 1. Show that modulo 2**31
#		I_n+2 - 6 * I_n+1 + 9 * I_n = 0
# 2. Implement RANDU and verify graphically its severse lack of equi-distribution by
#		creating a three dimensional plot of the 10,000 points for some odd I_0 of
#		your choice. More precisely, plot
#			{(I_n-1, I_n, I_n+1) / m} for n = 1, ..., 10,000
class RANDU:
	def __init__(self, seed):
		self.a = 65539
		self.c = 0
		self.m = 2**31
		self.seed = RANDU.set_seed(seed)
		self.nums = None
		self.vecs = None
# -----------
# MA 402: Project #2
# Adam Turner
# -----------
# Goal: Experiments with Monte Carlo integration. Introduction of quasi-random numbers.
# -----------
import random
import pandas as pd
import plotly.express as px

SEED = 11

# Problem 2
#	The infamous RANDU generator was part of the Scientific Subroutine Package on IBM
#	mainframe computers in the 1960's; the generator corresponds to
#		I_n+1 = (a * I_n + c) mod m,	n = 0, 1, ...
#	with a = 65539, c = 0 and m = 2**31.
# 1. Show that modulo 2**31
#		I_n+2 - 6 * I_n+1 + 9 * I_n = 0
# 2. Implement RANDU and verify graphically its severse lack of equi-distribution by
#		creating a three dimensional plot of the 10,000 points for some odd I_0 of
#		your choice. More precisely, plot
#			{(I_n-1, I_n, I_n+1) / m} for n = 1, ..., 10,000
class RANDU:
	def __init__(self, seed):
		self.a = 65539
		self.c = 0
		self.m = 2**31
		self.seed = RANDU.set_seed(seed)
		self.nums = None
		self.vecs = None

	@staticmethod
	def set_seed(seed):
		if seed % 2 == 0:
			seed += 1 
		return seed

	def generate_nums(self, max_n):
		I = self.seed
		nums = {}
		nums[0] = I
		for i in range(1, max_n+1):
			I = (self.a * I + self.c) % self.m
			nums[i] = I
		self.nums = nums

	def plot_equi_distr(self, points):
		self.vecs = []
		self.generate_nums(points+1)
		for i in range(1, points+1):
			self.vecs.append((self.nums[i-1], self.nums[i], self.nums[i+1]))
		self.vecs = pd.DataFrame(self.vecs, columns=['x', 'y', 'z']) / self.m
		fig = px.scatter_3d(self.vecs, x='x', y='y', z='z', color='y',
			title="RANDUmly generated points; seed=11, n=1, ..., 10000".format(self.seed))
		fig.update_traces(marker=dict(size=3))
		return fig.show()


randum = RANDU(SEED)
randum.plot_equi_distr(points=10000)

# compare against python pseudo-random numbers
random.seed(SEED)
r_dict = {}
for i in range(10002):
	r_dict[i] = random.random()
r_vecs = []
for i in range(1, 10001):
	r_vecs.append((r_dict[i-1], r_dict[i], r_dict[i+1]))
r_vecs = pd.DataFrame(r_vecs, columns=['x', 'y', 'z'])
fig = px.scatter_3d(r_vecs, x='x', y='y', z='z', color='y',
	title="Python 'random'ly generated points; seed={}; n=1, ... , 10000".format(SEED))
fig.update_traces(marker=dict(size=3))
fig.show()

	@staticmethod
	def set_seed(seed):
		if seed % 2 == 0:
			seed += 1 
		return seed

	def generate_nums(self, max_n):
		I = self.seed
		nums = {}
		nums[0] = I
		for i in range(1, max_n+1):
			I = (self.a * I + self.c) % self.m
			nums[i] = I
		self.nums = nums

	def plot_equi_distr(self, points):
		self.vecs = []
		self.generate_nums(points+1)
		for i in range(1, points+1):
			self.vecs.append((self.nums[i-1], self.nums[i], self.nums[i+1]))
		self.vecs = pd.DataFrame(self.vecs, columns=['x', 'y', 'z']) / self.m
		fig = px.scatter_3d(self.vecs, x='x', y='y', z='z', color='y',
			title="RANDUmly generated points; seed={}, n=1, ..., 10000".format(self.seed))
		fig.update_traces(marker=dict(size=3))
		return fig.show()


randum = RANDU(SEED)
randum.plot_equi_distr(points=10000)

# compare against python pseudo-random numbers
random.seed(SEED)
r_dict = {}
for i in range(10002):
	r_dict[i] = random.random()
r_vecs = []
for i in range(1, 10001):
	r_vecs.append((r_dict[i-1], r_dict[i], r_dict[i+1]))
r_vecs = pd.DataFrame(r_vecs, columns=['x', 'y', 'z'])
fig = px.scatter_3d(r_vecs, x='x', y='y', z='z', color='y',
	title="Python 'random'ly generated points; seed={}; n=1, ... , 10000".format(SEED))
fig.update_traces(marker=dict(size=3))
fig.show()
