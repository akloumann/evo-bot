from __future__ import print_function
from envs import ENVIRONMENTS
from pop import POPULATION
import const as c
import time
import pyrosim
import matplotlib.pyplot as plt
import numpy as np
import random
import copy
import pickle

class GENETIC_ALGORITHM:
    def __init__(self, fit_ids):
        fff = 1
        self.fit_ids = fit_ids

        # default x, y, popsize values for af_pareto()
        self.ymax = 15
        self.popsize = 25
        self.ys = np.random.randint(4, 15, self.popsize)
        self.xs = np.random.randint(0, self.popsize, self.popsize)

    ####################################################
    ####################### main #######################
    def main(self):
        num_rand = c.num_rand
        envs = ENVIRONMENTS()
        print('envs to run', c.envsToRun)
        parents = POPULATION(c.num_rand + len(self.fit_ids), 0)
        parents.InitializeRandomPop()
        for ind in range(0, num_rand + len(self.fit_ids)):
            print('ind', ind)

        self.af_pareto(self.xs, self.ys, self.popsize, self.ymax)
        parents = self.phc_ga(parents, envs, 3)  # like phc

        for j in range(0, len(parents.p)):
            raw_input('press enter to continue...')
            for e in c.envsToRun:
                # for j in range(0, 1):
                parents.p[j].Start_Evaluation(envs.envs[e], pp=True, pb=False, send=True)

    ####################### main #######################
    ####################################################

    def phc_ga(self, parents, envs, gens):
        for i in range (0, gens):
            children = copy.deepcopy(parents)
            children.Mutate()
            parents.Evaluate(envs, pp=False, pb=True)
            children.Evaluate(envs, pp=False, pb=True)
            print('******* Generation phc', i, '*******')
            parents.Print()
            children.Print(i)
            parents.ReplaceWith(children)
            parents.IncrementAges()
            print('New pop dists')
            parents.PrintDists(i)
        return parents


    def af_pareto_ga(self, parents, envs, gens):
        children = copy.deepcopy(parents)
        children.Mutate()
        parents.Evaluate(envs, pp=False, pb=True)
        children.Evaluate(envs, pp=False, pb=True)
        p_fits = parents.GetFits()
        c_fits = children.GetFits()



        return parents


    def af_pareto(self, xs, ys, popsize, ymax):
        ord_list = self.ord_list(0, popsize)
        checked_list = [False] * popsize
        dominated_list = [0] * popsize
        print('xs', xs, '\nys', ys, '\nol', ord_list, '\ncl', checked_list, '\ndl', dominated_list,'\n')
        for i in range(0, popsize):
            for j in range(0, popsize):
                if j == i: continue
                if ys[i] < ys[j] and xs[i] < xs[j]:
                    dominated_list[j] = 1
                elif ys[j] < ys[i] and xs[j] < xs[i]:
                    dominated_list[i] = 1
                    break
        print('dl', dominated_list)

        pareto_front_x = []
        pareto_front_y = []
        xx_copy = []
        yy_copy = []

        for i in range(0, popsize):
            if dominated_list[i] == 0:
                pareto_front_x.append(xs[i])
                pareto_front_y.append(ys[i])
            else:
                xx_copy.append(xs[i])
                yy_copy.append(ys[i])


        plt.figure(1)
        plt.subplot(211)
        plt.plot(xs, ys, 'ro')
        plt.xlim(-1, popsize)
        plt.ylim(-1, ymax)
        plt.subplot(212)
        plt.plot(pareto_front_x, pareto_front_y, 'bo')
        plt.plot(xx_copy, yy_copy, 'ro')
        plt.xlim(-1, popsize)
        plt.ylim(-1, ymax)
        plt.show()

    # high not inclusive
    def ord_list(self, low, high):
        list = []
        for i in range(low, high):
            print(i, end='  ')
            list.append(i)
        print()
        return list


fit_ids_load = []
start_ga = GENETIC_ALGORITHM(fit_ids_load)
start_ga.main()