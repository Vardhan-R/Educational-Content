import matplotlib.pyplot as plt, numpy as np

density = 11
ang = np.linspace(-np.pi, np.pi, density)
cos_ang = np.cos(ang)
sin_ang = np.sin(ang)
# n_1 = np.meshgrid(cos_ang, cos_ang)
# n_2 = np.meshgrid(cos_ang, sin_ang)
# n_3 = np.sin(ang)
# theta = np.linspace(-np.pi, np.pi, 11)
# phi = np.linspace(-np.pi, np.pi, 11)

theta, phi = np.meshgrid(ang, ang)

n_1 = np.outer(np.cos(theta), np.cos(phi))
n_2 = np.outer(np.cos(theta), np.sin(phi))
n_3 = np.outer(np.sin(theta), np.ones(density))
n = np.array([n_1.flatten(), n_2.flatten(), n_3.flatten()])
print(n.shape)
n.resize(3, density, density)

sigma_0 = np.array([0, 1, 1],
				   [1, 0, 1],
				   [1, 1, 0])

traction = np.dot(sigma_0, n)
print(traction.shape)

ax = plt.figure().add_subplot(projection="3d")
ax.plot_surface(theta, phi, np.sin(theta))
plt.show()