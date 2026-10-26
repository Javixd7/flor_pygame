
import numpy as np
from js import document

canvas = document.getElementById("lienzo")
ctx = canvas.getContext("2d")

ctx.fillStyle = "#080810"
ctx.fillRect(0, 0, 800, 600)

ctx.fillStyle = "#00e5ff"

for t in np.linspace(0, 2 * np.pi, 360):
    x = 400 + 180 * np.cos(float(t))
    y = 300 + 180 * np.sin(float(t))

    ctx.fillRect(x, y, 3, 3)
