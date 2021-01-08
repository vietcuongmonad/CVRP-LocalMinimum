import matplotlib.pyplot as plt
import numpy as np

def draw(y1, y2, x):
    x_axis = np.array(x)
    y1_axis = np.array(y1)
    y2_axis = np.array(y2)

    plt.plot(x_axis, y1_axis, marker='o', label='y1')
    plt.plot(x_axis, y2_axis, marker='*', label='y2')
    plt.xlabel('N')
    plt.ylabel('time')
    plt.legend()
    plt.show()
