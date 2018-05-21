import math

quick = 1
if quick == 0:
    fit_labels = []
    # fit_labels = [31118]
    popSize = 8
    evalTime = 850
    minutes = 0
    numGensDivPop = 0
    pathLoad = '/home/iskander/PycharmProjects/EvoBotProject2/genomes/run05040227/good/'
    pathSave = '/home/iskander/PycharmProjects/EvoBotProject2/genomes/'
    envsToRun = [2]
else:
    # fit_labels = [1370, 1451, 1468, 2067, 2235, 3021, 3386, 11824, 31118]
    # fit_labels = [6375, 10652, 3386, 11824, 31118]
    # fit_labels = [193]
    fit_labels = []
    popSize = 8
    evalTime = 100
    minutes = 0
    numGensDivPop = 1
    pathLoad = '/home/iskander/PycharmProjects/EvoBotProject2/genomes/run05040227/good/'
    pathSave = '/home/iskander/PycharmProjects/EvoBotProject2/genomes/'
    # envsToRun = [6, 7]
    envsToRun = [6]
    # envsToRun = [1]

num_rand = 5
numEnvs = len(envsToRun)
fitness_scale = 10**7

numInputs = 17
numHidden = 12
numOutputs = 9

L = 0.13
R = L/5
# Pi = 3.14159

cutoff = 3

popSizeGA1 = 10
numGensGA1 = 1

angle_range_deg = 140
angle_range = math.pi * angle_range_deg / 180

fitPenMult = 0.7

upJointHalfRange = math.pi/3
lowJointHalfRange = math.pi/2

maxAvgAngUpJ = upJointHalfRange / 2
maxAvgAngLoJ = lowJointHalfRange / 2

lightDistMult = 20
lightDist = lightDistMult * L
lightSrcL = L
lightSrcW = L
lightSrcH = 4.7 * L

numObstacles = 7
obstacles = True

wallDist = lightDist / 2.8

obstL = 0.5 * L
obstW = 0.5 * L
obstH = 3 * L

####### Wall #######
wallL = wallDist * 2
wallW = L
wallH = 2.5 * L
wallCutFrac = 0.7
wallCut = wallDist * wallCutFrac

bodyAngDeg = 45; bodyAng = math.pi*bodyAngDeg/180


mutateRandFreq = 15
numBigMutate = 2
mutateFreq = 20

spinSpeed = 4

pickleFreq = 1

sigfigs = 2

def round_matrix(h):
    for i in range(0, len(h)):
        for j in range(0, len(h[i])):
            h[i][j] = round(h[i][j], sigfigs)
    return h