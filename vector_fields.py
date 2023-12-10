import matplotlib.pyplot as plt, numpy as np

density = 31
x = np.linspace(-5, 5, density)
y = np.linspace(-5, 5, density)

x_mesh, y_mesh = np.meshgrid(x, y)

# u = y_mesh / x_mesh + 6 * x_mesh
# v = np.log(np.abs(x_mesh)) - 2
u = 3 * y_mesh ** 2
v = 2 * x_mesh ** 3
# u = 2 * x_mesh + 3
# v = 2 * y_mesh - 2
# u = 3 * x_mesh ** 2 + 6 * x_mesh * y_mesh ** 2
# v = 6 * x_mesh ** 2 * y_mesh + 4 * y_mesh ** 3
# u = 3 * x_mesh ** 2 * y_mesh + 2 * x_mesh * y_mesh + y_mesh ** 3
# v = x_mesh ** 2 + y_mesh ** 2
# u = (3 * x_mesh ** 2 * y_mesh ** 3 - y_mesh ** 2 + y_mesh) / x_mesh ** 2 / y_mesh ** 3
# v = (-x_mesh * y_mesh + 2 * x_mesh) / x_mesh ** 2 / y_mesh ** 3
# u = -2 * y_mesh
# v = x_mesh

density = 999
x = np.linspace(-5, 5, density)
y = np.linspace(-5, 5, density)

x_mesh, y_mesh = np.meshgrid(x, y)

c = 0.2
# sol = y_mesh * np.log(np.abs(x_mesh)) + 3 * x_mesh ** 2 - 2 * y_mesh
sol = -4 / y_mesh - 3 / x_mesh ** 2
# sol = x_mesh ** 2 + 3 * x_mesh + y_mesh ** 2 - 2 * y_mesh
# sol = x_mesh ** 3 + 3 * x_mesh ** 2 * y_mesh ** 2 + y_mesh ** 4
# sol = y_mesh * (x_mesh ** 2 + y_mesh ** 2 / 3) * np.exp(3 * x_mesh)
# sol = 1 / x_mesh / y_mesh ** 2 * (y_mesh - 1) + 3 / 5 * x_mesh
# sol = y_mesh / x_mesh ** 2

mag = np.sqrt(u ** 2 + v ** 2)
u /= mag
v /= mag

density = 31
x = np.linspace(-5, 5, density)
y = np.linspace(-5, 5, density)

x_mesh, y_mesh = np.meshgrid(x, y)

qq = plt.quiver(x_mesh, y_mesh, u, v, mag, scale=density, cmap=plt.cm.turbo)
plt.colorbar(qq, cmap=plt.cm.turbo)
# plt.plot(x, y_sol)
# plt.title("Vector Field and Solution Contour")
# plt.contour(x_mesh, y_mesh, sol, [c], colors=["red"])
plt.title("Vector Field and Solution Contour Field")
plt.contourf(x_mesh, y_mesh, sol, np.linspace(1, 10, 10), cmap="magma")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect("equal", "box")
plt.show()

ax = plt.figure().add_subplot(projection="3d")
ax.plot_surface(x_mesh, y_mesh, sol, edgecolor="royalblue", lw=0.5, rstride=1, cstride=1, alpha=0.3)
ax.set(xlabel='$x$', ylabel='$y$', zlabel='$G\\left(x,y\\right)$')
plt.show()