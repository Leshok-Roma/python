import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
plt.axis('off')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

def circle(x, y, r, color):
    ax.add_patch(patches.Circle((x, y), r, color=color, ec="black", lw=2))

def ellipse(x, y, w, h, color):
    ax.add_patch(patches.Ellipse((x, y), w, h, color=color, ec="black", lw=2))

def triangle(points, color):
    ax.add_patch(patches.Polygon(points, closed=True, color=color, ec="black", lw=2))

def arc(x, y, w, h, t1, t2):
    ax.add_patch(patches.Arc((x, y), w, h, theta1=t1, theta2=t2, lw=2))


circle(0, 0.5, 2.4, "orange")
circle(0, 1.0, 1.6, "gold")

triangle([(-1.0, 2.0), (-1.5, 2.8), (-0.5, 2.7)], "gold")
triangle([( 1.0, 2.0), ( 1.5, 2.8), ( 0.5, 2.7)], "gold")

circle(-0.55, 1.45, 0.35, "white")
circle( 0.55, 1.45, 0.35, "white")

circle(-0.35, 1.50, 0.12, "black")
circle( 0.35, 1.50, 0.12, "black")

triangle([(-0.25, 1.1), (0.25, 1.1), (0, 1.25)], "black")

arc(0, 1.0, 0.9, 0.6, 230, 310)
arc(0, 1.0, 0.9, 0.6, 350, 430)

ellipse(0, -1.2, 3.0, 3.8, "gold")
ellipse(-0.9, -2.6, 1.1, 0.55, "gold")
ellipse( 0.9, -2.6, 1.1, 0.55, "gold")

plt.show()
