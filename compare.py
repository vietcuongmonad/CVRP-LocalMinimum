import solution_origin
import solution_new
import generate_tests
import time
import sys

num_test = 10
N_list = generate_tests.create_test(num_test)

t_origin = []
mileage_origin = []
unbalance_origin = []

t_new = []
mileage_new = []
unbalance_new = []

origin_stdin = sys.stdin
origin_stdout = sys.stdout

for i in range(num_test):
    f_inp = open('experiment/input' + str(i+1) + '.txt', 'r')
    f_out_origin = open('experiment/out_origin' + str(i+1) + '.txt', 'w')

    sys.stdin = f_inp
    sys.stdout = f_out_origin

    tmp_origin = time.time()

    mileage, workload = solution_origin.algorithm()

    t_origin += [time.time() - tmp_origin]
    mileage_origin += [mileage]
    unbalance_origin += [workload]

    sys.stdin = origin_stdin
    sys.stdout = origin_stdout

    f_inp.close()
    f_out_origin.close()

    f_inp = open('experiment/input' + str(i+1) + '.txt', 'r')
    f_out_new = open('experiment/out_new' + str(i+1) + '.txt', 'w')

    sys.stdin = f_inp
    sys.stdout = f_out_new

    tmp_new = time.time()

    mileage, workload = solution_new.algorithm()

    t_new += [time.time() - tmp_new]
    mileage_new += [mileage]
    unbalance_new += [workload]

    sys.stdin = origin_stdin
    sys.stdout = origin_stdout

    f_inp.close()
    f_out_new.close()

import matplotlib.pyplot as plt
import numpy as np

def draw(y1, y2, x, text, file_name):
    x_axis = np.array(x)
    y1_axis = np.array(y1)
    y2_axis = np.array(y2)

    plt.plot(x_axis, y1_axis, marker='o', label='origin')
    plt.plot(x_axis, y2_axis, marker='*', label='new')
    plt.xlabel('N')
    plt.ylabel(text)
    plt.legend()
    plt.savefig(file_name)
    plt.show()

draw(t_origin, t_new, N_list, 'time (s)', 'pic_runtime.png')
draw(mileage_origin, mileage_new, N_list, 'mileage (km)', 'pic_mileage.png')
draw(unbalance_origin, unbalance_new, N_list, 'unbalance_workload', 'pic_unbalance.png')
