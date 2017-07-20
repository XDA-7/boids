import tkinter
import time
top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg = 'grey', height = 1000, width = 1000)
canvas.pack()

coords = 10,50,240,210
arc = canvas.create_arc(coords, start = 0, extent = 150, fill = 'red')

while True:
    #time.sleep(1)
    canvas.move(arc, 10, 0)
    top.update()
#top.mainloop()