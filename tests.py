from __future__ import print_function
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import copy

class Tests:
    def __init__(self):
        g = 7

    def main(self):

        high = 15
        size = 259

        yy = np.random.randint(4, 15, size)
        xx = np.random.randint(0, size, size)

        ord_list = self.ord_list(0, size)
        checked_list = [False] * size
        dominated_list = [0] * size

        print('xx', xx, '\nyy', yy, '\nol', ord_list, '\ncl', checked_list, '\ndl', dominated_list)
        print()

        for i in range(0, size):
            for j in range(0, size):
                if j == i:
                    continue
                if yy[i] < yy[j] and xx[i] < xx[j]:
                    dominated_list[j] = 1
                elif yy[j] < yy[i] and xx[j] < xx[i]:
                    dominated_list[i] = 1
                    break
        print('dl', dominated_list)

        pareto_front_x = []
        pareto_front_y = []
        xx_copy = []
        yy_copy = []

        for i in range(0, size):
            if dominated_list[i] == 0:
                pareto_front_x.append(xx[i])
                pareto_front_y.append(yy[i])
            else:
                xx_copy.append(xx[i])
                yy_copy.append(yy[i])


        plt.figure(1)
        plt.subplot(211)
        plt.plot(xx, yy, 'ro')
        plt.xlim(-1, size)
        plt.ylim(-1, high)
        plt.subplot(212)
        plt.plot(pareto_front_x, pareto_front_y, 'bo')
        plt.plot(xx_copy, yy_copy, 'ro')
        plt.xlim(-1, size)
        plt.ylim(-1, high)
        plt.show()

    def tups(self, y):
        tuples = []
        for i in range(0, len(y)):
            tuples.append((i, y[i]))
        print(tuples)
        return tuples

    # high not inclusive
    def ord_list(self, low, high):
        list = []
        for i in range(low, high):
            print(i, end='  ')
            list.append(i)
        print()
        return list


u = Tests()
u.main()
