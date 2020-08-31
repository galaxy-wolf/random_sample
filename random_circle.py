import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
a_circle = plt.Circle((0, 0), 1.0)
ax.add_artist(a_circle)
ax.set_aspect('equal', adjustable='datalim')
plt.show()