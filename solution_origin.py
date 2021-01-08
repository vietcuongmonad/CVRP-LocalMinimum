''' In this problem scope
    insert tmp at position i mean put tmp between (i, i+1)
'''

import math

def algorithm():
    def dist(point_a, point_b):
        tmp1 = point_a[0] - point_b[0]
        tmp2 = point_a[1] - point_b[1]
        return int(math.sqrt(tmp1*tmp1 + tmp2*tmp2))+2  # Distance between 2 point

    def convert(st): # Concatenate all number in string -> convert to int
        res = ''
        for _ in st:
            if ('0' <= _ and _ <= '9'):
                res+=_
        return int(res)

    def read_input():
        s = []
        f = []
        w = []
        loc = []
        cap = []

        N = int(input())

        for i in range(N):
            tmp = input().split()
            s+=[(convert(tmp[0]), convert(tmp[1]))]
            f+=[(convert(tmp[2]), convert(tmp[3]))]
            w+=[convert(tmp[4])]

        M = int(input())

        for i in range(M):
            tmp = input().split()
            loc+=[(convert(tmp[0]), convert(tmp[1]))]
            cap+=[convert(tmp[2])]

        return N, s, f, w, M, loc, cap

    def init():
        mileage = [0] * M
        sum_mileage = 0
        schedule = []
        assign = [-1] * N

        for i in range(M):
            schedule+=[[(0, 0), (0, 0)]]

        return mileage, sum_mileage, schedule, assign

    def locate(id, pos_car):
        if (id == 0): return loc[pos_car]
        if (id > 0): return s[id-1]
        return f[-id-1]

    def tryout(pos_item, pos_car):
        weight = w[pos_item]
        capacity = cap[pos_car]

        if weight > capacity: return (-1, -1, -1)

        calendar = schedule[pos_car]
        leng = len(calendar)
        delta, tmp_s, tmp_f = (-1, -1, -1)

        for k in range(leng-1):
            #Case 1: insert both _s and _f in k
            if calendar[k][1] + weight > capacity: continue

            point_a = locate(calendar[k][0], pos_car)
            point_b = locate(calendar[k+1][0], pos_car)

            increase = dist(point_a, s[pos_item]) + dist(s[pos_item], f[pos_item])
            increase += dist(f[pos_item], point_b) - dist(point_a, point_b)

            if (delta == -1 or delta > increase):
                delta = increase
                tmp_s = k
                tmp_f = k

            #Case 2: insert _s at k, _f > k
            big_w = calendar[k][1]

            add_k = dist(point_a, s[pos_item]) + dist(s[pos_item], point_b)
            add_k -= dist(point_a, point_b)

            for h in range(k+1, leng-1):
                big_w = max(big_w, calendar[h][1])
                if big_w + weight > capacity: break

                point_c = locate(calendar[h][0], pos_car)
                point_d = locate(calendar[h+1][0], pos_car)

                add_h = dist(point_c, f[pos_item]) + dist(f[pos_item], point_d)
                add_h -= dist(point_c, point_d)

                if (delta == -1 or delta > add_h + add_k):
                    delta = add_h+add_k
                    tmp_s, tmp_f = (k, h)

        return delta, tmp_s, tmp_f

    def exec(pos_item, pos_car, pos_s, pos_f):
        assign[pos_item] = pos_car
        weight = w[pos_item]

        calendar = schedule[pos_car]
        calendar.insert(pos_s+1, (pos_item+1, calendar[pos_s][1]+weight))

        pos_f += 1
        for i in range(pos_s+2, pos_f+1):
            calendar[i] = (calendar[i][0], calendar[i][1]+weight)

        calendar.insert(pos_f+1, (-(pos_item+1), calendar[pos_f][1]-weight))
        schedule[pos_car] = calendar

    def print_out(schedule): # Output of the code
        print('Total travel mileage: ', sum_mileage)

        print('Schedule of all car:')
        print(' -> (u, v) here means (current location, current capacity)')
        print(' u = 0 -> original location of car, u > 0 -> start-point of item u, u < 0 -> end-point of item -u')
        for i in range(len(schedule)):
            print('Schedule for car ' + str(i+1) + ':')
            for j in range(len(schedule[i])):
                print(schedule[i][j], end=' ')
            print()

    #   Algorithms

    N, s, f, w, M, loc, cap = read_input()

    mileage, sum_mileage, schedule, assign = init()

    while True:
        increase = -1

        u, v = (-1, -1)
        pos_s, pos_f = (-1, -1)

        for i in range(N):
            if (assign[i] == -1):
                for j in range(M):
                    delta, tmp_s, tmp_f = tryout(i, j)

                    if (delta >= 0):
                        if (increase == -1 or increase > delta):
                            increase = delta
                            u, v = (i, j)
                            pos_s, pos_f = (tmp_s, tmp_f)

        if (increase != -1):
            exec(u, v, pos_s, pos_f)
            sum_mileage+= increase
        else: break;

    print_out(schedule)

    average = int(N / M)
    workload = 0
    for _ in range(M): workload += abs(len(schedule[_]) // 2 - average)

    return (sum_mileage, workload)

if __name__ == '__main__':
    algorithm()
