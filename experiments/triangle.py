import time
import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(window, height=1000, width=1000)
canvas.pack()

bottom_y = 600
triangle = canvas.create_polygon(400, 400, 600, 400, 500, 600)

for i in range(1, 200):
    window.update()
    bottom_y += 1
    canvas.delete(triangle)
    triangle = canvas.create_polygon(400, 400, 600, 400, 500, bottom_y)
    time.sleep(0.1)
