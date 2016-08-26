import numpy as np


nicks = 'Victoria kash Jhon Tim Jemma Ian Andy Spman Ironman'.split()
run = 10000000
a = np.array([1,2,2,2,2,3,3,3,3,3,3,45,45,4,54,5,44,5,45,4])

print np.nonzero(np.bincount(a))[0]

uniq_keys = np.unique(a)
bins = uniq_keys.searchsorted(a)

print uniq_keys , bins