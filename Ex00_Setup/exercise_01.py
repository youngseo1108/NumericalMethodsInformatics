import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figwidth(12)
fig.set_figheight(5)

vf = np.array([1., 0.])
vb = np.array([1., 0.])
# 5° per turn
angle = 5. * np.pi / 180.
A = np.array([[np.cos(angle), np.sin(angle)], [-np.sin(angle), np.cos(angle)]])
qf = ax1.quiver(0, 0, 1, 0)
qb = ax2.quiver(0, 0, 1, 0)

def init():
  ax1.set_xlim(-1.05, 1.05)
  ax1.set_ylim(-1.05, 1.05)
  ax1.grid(True)
  ax1.set_title("Forward Iteration")
  ax2.set_xlim(-1.05, 1.05)
  ax2.set_ylim(-1.05, 1.05)
  ax2.grid(True)
  ax2.set_title("Backward Iteration")
  return None,

def forwardAnimation(t):
  global vf, qf
  tmp = A.dot(vf)
  vf = tmp
  qf.remove()
  qf = ax1.quiver(0, 0, vf[0], vf[1], angles='xy', scale=1, scale_units='xy')
  return None,

def backwardAnimation(t):
  global vb, qb
  # There are much better ways to do this
  tmp = np.linalg.solve(A, vb)
  vb = tmp
  qb.remove()
  qb = ax2.quiver(0, 0, vb[0], vb[1], angles='xy', scale=1, scale_units='xy')
  return None,



ani1 = animation.FuncAnimation(fig, 
                              forwardAnimation,
                              interval=50,
                              init_func=init)

ani2 = animation.FuncAnimation(fig, 
                              backwardAnimation,
                              interval=50,
                              init_func=init)
plt.show()


