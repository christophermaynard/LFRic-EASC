import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt

# Script to created figures of the dof locations for the finite element spaces used in gungho

points = np.array([[-1, -1, -1],
                  [1, -1, -1 ],
                  [1, 1, -1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [1, -1, 1 ],
                  [1, 1, 1],
                  [-1, 1, 1]])
Z = np.zeros((8,3))
for i in range(8): Z[i,:] = points[i,:]

# list of sides' polygons of figure
verts = [[Z[0],Z[1],Z[2],Z[3]],
 [Z[4],Z[5],Z[6],Z[7]], 
 [Z[0],Z[1],Z[5],Z[4]], 
 [Z[2],Z[3],Z[7],Z[6]], 
 [Z[1],Z[2],Z[6],Z[5]],
 [Z[4],Z[7],Z[3],Z[0]], 
 [Z[2],Z[3],Z[7],Z[6]]]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = [-1,1]

X, Y = np.meshgrid(r, r)
# plot vertices
ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2], s=100)


# plot sides
ax.add_collection3d(Poly3DCollection(verts, 
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_zlim(-1.1, 1.1)
ax.axis('off')

plt.savefig('W0_dofs.pdf')

# W2 dofs
fig1 = plt.figure()
bx = fig1.add_subplot(111, projection='3d')

faces = np.array([[-1, 0, 0],
                  [ 1, 0, 0],
                  [ 0, -1, 0],
                  [ 0, 1, 0],
                  [ 0, 0, -1],
                  [ 0, 0, 1]])
normals = ["v", "^", "<", ">", "<", ">"]
bx.scatter3D(faces[:, 0], faces[:, 1], faces[:, 2], s=100, marker="^")

# plot sides
bx.add_collection3d(Poly3DCollection(verts, 
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
bx.set_xlim(-1.1, 1.1)
bx.set_ylim(-1.1, 1.1)
bx.set_zlim(-1.1, 1.1)
bx.axis('off')

plt.savefig('W2_dofs.pdf')

# W1 dofs
fig2 = plt.figure()
cx = fig2.add_subplot(111, projection='3d')

edges = np.array([[-1, -1, 0],
                  [ 1, -1, 0],
                  [-1, 1, 0],
                  [ 1, 1, 0],
                  [ 0, -1, -1],
                  [ 0, -1, 1],
                  [ 0, 1, -1],
                  [ 0, 1, 1],
                  [ -1, 0, -1],
                  [ -1, 0, 1],
                  [ 1, 0, -1],
                  [ 1, 0, 1]])
cx.scatter3D(edges[:, 0], edges[:, 1], edges[:, 2], s=100, marker="^")

# plot sides
cx.add_collection3d(Poly3DCollection(verts, 
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
cx.set_xlim(-1.1, 1.1)
cx.set_ylim(-1.1, 1.1)
cx.set_zlim(-1.1, 1.1)
cx.axis('off')

plt.savefig('W1_dofs.pdf')

# W3 dofs
fig3 = plt.figure()
dx = fig3.add_subplot(111, projection='3d')
dx.scatter3D(0.0,0.0,0.0, s=100)

# plot sides
dx.add_collection3d(Poly3DCollection(verts, 
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
dx.set_xlim(-1.1, 1.1)
dx.set_ylim(-1.1, 1.1)
dx.set_zlim(-1.1, 1.1)
dx.axis('off')

plt.savefig('W3_dofs.pdf')

