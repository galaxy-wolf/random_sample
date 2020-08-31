import matplotlib.pyplot as plt
import random
import math
fig, ax = plt.subplots()

def random_sample_circle_inverse_cdf():
    r = math.sqrt(random.random())
    theta = random.random() * 2 * math.pi
    return (math.sin(theta) * r, math.cos(theta) * r)

def random_sample_square():
    return [random.random()*2.0-1, random.random()*2.0-1]

def random_sample_circle_reject():
    p = random_sample_square()
    x, y = p[0], p[1]
    while(x*x+y*y > 1.0):
        p = random_sample_square()
        x, y = p[0], p[1]
    return p


ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
a_circle = plt.Circle((0, 0), 1.0)
ax.add_artist(a_circle)
ax.set_aspect('equal', adjustable='datalim')

NUM = 1000
plist = []
for i in xrange(0, NUM):
    # plist.append(random_sample_square())
    # plist.append(random_sample_circle_reject())
    plist.append(random_sample_circle_inverse_cdf())
plt.plot(*zip(*plist), marker='o', color='r', ls='', markersize=2)

plt.show()