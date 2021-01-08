import random
import math
import os, glob

def create_test(num_test = 1):
    for f in glob.glob('experiment/input*.txt'):
        os.remove(f)

    for f in glob.glob('experiment/out*.txt'):
        os.remove(f)

    map_range = 100
    max_N = 200
    max_M = 10
    max_w = 100

    start_N = max_N // num_test

    delta = 0
    if num_test > 1: delta = int((max_N - start_N) / (num_test-1) )

    random.seed()

    def birth(x):   #random from 0 -> x-1
        return random.randint(0, x-1)

    def dist(point_a, point_b):
        tmp1 = point_a[0] - point_b[0]
        tmp2 = point_a[1] - point_b[1]
        return int(math.sqrt(tmp1*tmp1 + tmp2*tmp2))+1

    N = start_N
    N_list = []

    for id in range(num_test):
        file_name = open('experiment/input' + str(id+1) + '.txt', 'w')

        print(N, file=file_name)
        N_list += [N]

        # Generate N request

        big_package = 0

        for i in range(N):
            while True:
                s = (birth(map_range), birth(map_range))
                f = (birth(map_range), birth(map_range))
                if (f == s): continue

                w = birth(max_w)

                big_package = max(big_package, w)
                print(s, f, w, file=file_name)
                break

        M = birth(max_M) + 1
        M = max_M
        print(M, file=file_name)

        big_vehicle = 0

        for i in range(M):
            location = (birth(map_range), birth(map_range))

            cap = birth(max_w)
            big_vehicle = max(big_vehicle, cap)

            if (big_vehicle < big_package and i == M-1):
                cap = big_package + 1

            print(location, cap, file=file_name)

        N += delta

    return N_list

if __name__ == '__main__':
    create_test()
