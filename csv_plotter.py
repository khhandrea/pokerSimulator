import matplotlib.pyplot as plt
from time import sleep

data = list(map(int, open('data.csv').readlines()[0].split(', ')))
category = "high, one, two, tripple, straight, flush, fullhouse, 4card, stfl, rofl".split(', ')

def update_graph():
    plt.barh(category, data)
    plt.show()

fig, ax = plt.subplots()
rects = ax.barh(category, data)

for i in range(5):
    data = list(map(int, open('data.csv').readlines()[0].split(', ')))
    rects = ax.barh(category, data)

    plt.cla()
    for rect,h in zip(rects, data):
        rect.set_width(h)
    fig.canvas.draw()
    print('plot')
    
    plt.pause(0.5)