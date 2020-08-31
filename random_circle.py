import matplotlib.pyplot as plt
import random
fig, ax = plt.subplots()

def random_sample_circle_reject():
    return (0, 0)

def random_sample_circle_inverse_cdf():
    return (0, 0)

def random_sample_square():
    return [random.random()*2.0-1, random.random()*2.0-1]


ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
a_circle = plt.Circle((0, 0), 1.0)
ax.add_artist(a_circle)
ax.set_aspect('equal', adjustable='datalim')

NUM = 1000
plist = []
for i in xrange(0, NUM):
    plist.append(random_sample_square())
plt.plot(*zip(*plist), marker='o', color='r', ls='', markersize=2)

plt.show()