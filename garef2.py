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


### new
# parents0 = POPULATION(100)
# parents0.Initialize()
# parents0.Evaluate(envs, pp=False, pb=True)
# parents0.Print()
# print('********************* done')
### new end



i = 0
t_end = time.time() + 60 * c.minutes

envs = ENVIRONMENTS()
parentsF = POPULATION(len(c.fit_labels), -1)

fit_labels = copy.deepcopy(c.fit_labels)
num_rand = c.num_rand
print('fit labels', fit_labels)
print('envs to run', c.envsToRun)

for k in range(0, len(c.fit_labels) + num_rand):
    print('**********************\nindividual num', k, 'begin\n**********************')
    parents = POPULATION(c.popSize, -1)
    if k < num_rand:
        first = np.random.random_sample((c.numInputs, c.numHidden)) * 2 - 1
        second = np.random.random_sample((c.numHidden, c.numOutputs)) * 2 - 1
        genome = [first, second]
    else:
        filename = 'genome' + str(fit_labels[0])
        del fit_labels[0]
        pathLoad = c.pathLoad
        filename = pathLoad + filename
        g = open(filename, 'r')
        genome = pickle.load(g)
        g.close()

    parents.InitializeUniformPop(genome)
    parents.Evaluate(envs, pp=False, pb=True)
    parents.Print(-1)
    dists = []
    fits = []
    for i in range(0, c.numGensDivPop):
        # the POPULATION constructor creates an empty dictionary and stores the variable popSize
        children = POPULATION(c.popSize, i)
        # children.Print('bm')
        print()
        children.FillFrom(parents)

        print('seconds remaining', t_end - time.time())

        # print('\n0', end=' ')
        parents.Print()
        children.Evaluate(envs, pp=False, pb=True)
        # print(i, end=' ')
        children.Print(i)
        children.PrintDists(i)
        parents = children
        dists.append(parents.p[0].distTarget[-1])
        fits.append(parents.p[0].fitness)

        # ############### knocked check maybe uncomment ###############
        # for ii in c.envsToRun:
        #     print('env knocked check', envs.envs[ii].knocked_check)

    parentsF.p[k] = copy.deepcopy(parents.p[0]); parentsF.p[k].ID = k
    parentsF.Print('final pop from ga\n')

plt.figure(2)
plt.subplot(211)
plt.plot(dists)
plt.ylim((0, 2.5))
plt.ylabel('distance to target')
plt.xlabel('generation')

plt.subplot(212)
plt.plot(fits)
# plt.ylim((0, 2.5))
plt.ylabel('fitness')
plt.xlabel('generation')

plt.show()

for j in range(0, len(parentsF.p)):
    raw_input('press enter to continue...')
    for e in c.envsToRun:
    # for j in range(0, 1):
        parentsF.p[j].Start_Evaluation(envs.envs[e], pp=True, pb=False, send=True)


# plt.figure(2)
# plt.subplot(211)
# plt.plot(parents.p[0].propData7)
# plt.ylim((-0.7, 0.7))
# plt.ylabel('joint angle')
# plt.xlabel('time step')

# print('################ Begin parallel hill climber ######################')
# parentsF.Print('start pop phc')

# parentsF.Initialize()

# envs = ENVIRONMENTS()


# # for i in range(0,3):
# while time.time() < t_end:
#     # print('############# i', i)
#     print('secs remaining', t_end - time.time())
#     print('\nF', end='')
#     parentsF.Print()
#     childrenF = copy.deepcopy(parentsF)
#     childrenF.Mutate()
#     childrenF.Evaluate(envs, pp=False, pb=True)
#     print('F', end='')
#     childrenF.Print(i)
#     parentsF.ReplaceWith(childrenF)
#     print('W', end='')
#     parentsF.Print(i)
#     parentsF.PrintDists(i)
#
#     # for k in c.envsToRun:
#     #     print('env knocked check', envs.envs[k].knocked_check)
#
#     i += 1
#
#     if i % 50 == 0:
#         parentsF.Pickling(parentsF)


# print('fit labels', c.fit_labels)
# print('envs to run', c.envsToRun)


# plt.subplot(412)
# plt.plot(parents.p[0].propData2)
# plt.ylabel('angle joint 2')
# plt.xlabel('time step')
# plt.subplot(421)
# plt.plot(parents.p[0].propData4)
# plt.ylabel('angle joint 4')
# plt.xlabel('time step')
# plt.subplot(422)
# plt.plot(parents.p[0].propData6)
# plt.ylabel('angle joint 6')
# plt.xlabel('time step')

plt.show()





###########################################
# UNCOMMENT!
# plt.figure(1)
# plt.subplot(411)
# plt.plot(parents.p[0].distOrg)
# plt.ylabel('distance')
# plt.subplot(412)
# plt.plot(parents.p[0].speed)
# plt.ylabel('speed')
# plt.subplot(413)
# plt.plot(parents.p[0].distTarget)
# plt.ylabel('dist target')
# plt.subplot(414)
# plt.plot(parents.p[0].vestibularSensorDataBox)
# plt.ylabel('vest sens body')
#
# plt.figure(2)
# plt.subplot(411)
# plt.plot(parents.p[0].propData0)
# plt.ylabel('joint 0 red')
# plt.subplot(412)
# plt.plot(parents.p[0].propData2)
# plt.ylabel('joint 2 green')
# plt.subplot(413)
# plt.plot(parents.p[0].propData4)
# plt.ylabel('joint 4 blue')
# plt.subplot(414)
# plt.plot(parents.p[0].propData6)
# plt.ylabel('joint 6 purple')
#
# plt.show()
###########################################

#########################################
# print(parents.p[0].genome)
# genome = parents.p[0].genome
# print('fitness to pickle:', parents.p[0].fitness)
#
# filename = 'bot' + str(parents.p[0].fitness)
# fullPath = '/home/iskander/PycharmProjects/EvoBotProject/genomes/'
# filename = fullPath + filename
# e = open(filename, 'w')
# pickle.dump(genome, e)
# e.close()
#
# g = open(filename, 'r')
# newGenome = pickle.load(g)
# print('Again\n', newGenome)

# DILL.pickleGenome(parents)
#
# class DILL:
#     @staticmethod
#     def pickleGenome(parents):
#         genome = parents.p[0].genome
#         print('fitness to pickle:', parents.p[0].fitness)
#         e = open('bot.p', 'w')
#         pickle.dump(genome, e)
#         e.close()
#
#         g = open('bot.p', 'r')
#         newGenome = pickle.load(g)
#     print('Again\n', newGenome)
########################################

# f = open('robot.p', 'w')
# pickle.dump(parents, f)
# f.close

# f = plt.figure()
# panel = f.add_subplot(131)
# # panel.set_ylim(-2, 0.5)
# plt.plot(y)
# panel = f.add_subplot(132)
# plt.plot(z)
# plt.show()
