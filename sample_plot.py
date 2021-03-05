import tkinter as tk
import numpy as np
import time

data = [420, 452, 67, 49, 3, 3, 5, 1, 0, 0]

root = tk.Tk()
root.title("Bar Graph")

canvas_width = 400  # Define it's width
canvas_height = 350  # Define it's height
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

plot_width = 350
plot_height = 300
plot_x = 25
plot_y = 25
x_gap = 30
bar_width = 15
max_data = np.max(data)

for y, x in enumerate(data):
    x0 = plot_x + x_gap
    y0 = plot_height*(y+1)/(len(data)) - (bar_width/2)
    x1 = x0 + data[y]*(plot_width-2*x_gap)/max_data
    y1 = plot_height*(y+1)/(len(data)) + (bar_width/2)
    tag_name = "rect" + str(y)
    canvas.create_rectangle(x0, y0, x1, y1, fill="red", outline="", tags=tag_name)

time.sleep(1)

# for y in range(len(data)):
#     tag_name = "rect" + str(y)
#     canvas.delete(tag_name)
    

root.mainloop()