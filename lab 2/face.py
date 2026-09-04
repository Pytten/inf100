
from uib_inf100_graphics.simple import canvas, display

canvas.create_oval(125, 250, 250, 125)
canvas.create_oval(140, 200, 160, 180)
canvas.create_oval(215, 200, 235, 180)
canvas.create_arc(160, 210, 215, 240, start=160, extent =215)


display(canvas)