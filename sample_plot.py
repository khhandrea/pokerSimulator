import numpy as np
import matplotlib.pyplot as plt

label = ['Thur', 'Fri', 'Sat', 'Sun']
index = np.arange(len(label))
plt.barh(index, tips_sum_by_day)
plt.title('Sum of Tips by Day', fontsize=18)
plt.ylabel('Day', fontsize=15)
plt.xlabel('Sum of Tips', fontsize=15)
plt.yticks(index, label, fontsize=13, rotation=0)
plt.show()