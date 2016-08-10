import numpy as np

nwalks = 30
nsteps = 20
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws>0, 1, -1)
walks = steps.cumsum(1)
print walks
hit30 = (np.abs(walks)>=5).any(1)
print hit30
print hit30.sum()
crossing_time = (np.abs(walks[hit30])>=5).argmax(1)
print crossing_time