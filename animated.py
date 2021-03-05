import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

objects = ("google","ibm","kaspersky","amazon","facebook","sony","microsoft","apple")

def update_graph():
    fig.clear()
    cols = ["google","ibm","kaspersky","amazon","facebook","sony","microsoft","apple"]
    df = pd.read_csv("filepath",header=None,  names=cols,encoding = "UTF-8",low_memory=False)
    y_pos = np.arange(len(objects))
    performance = df.values.tolist()
    flat_list = [item for sublist in performance for item in sublist]
    plt.bar(y_pos, flat_list, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('s (%)')
    fig.canvas.draw() # clear canvas
    win.after(20000, update_graph) # after(delay time, function to launch)

fig = plt.figure()
win = fig.canvas.manager.window
update_graph()
plt.show()