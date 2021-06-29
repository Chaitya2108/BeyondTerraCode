import numpy as np 
import matplotlib.pyplot as plt 
import math
 
angle = np.linspace( 0 , 2 * np.pi , 150 ) 
 
radius = 10
hl = [0, 0]
 
x = radius * np.cos( angle ) 
y = radius * np.sin( angle ) 
 
figure, axes = plt.subplots( 1 ) 
 
axes.plot( x, y ) 
axes.set_aspect( 1 ) 
 
plt.title( 'Parametric Equation Circle' ) 

z = 1

hl = [hl[0]-radius, hl[1]]
for i in range (2*(radius // z)):
    cl = [hl[0]+z, hl[1]]
    plt.plot(cl[0], cl[1], color="blue", marker='o')
    hl = cl

hl = [0,0]
for x in range (1, (radius)+1):
    cl = [hl[0], hl[1]+z]
    plt.plot(cl[0], cl[1], color="blue", marker='o')
    # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')
    hl = cl
    chordlength = math.sqrt((radius)**2 - (x)**2)
    print(chordlength)
    numofiterations = chordlength // z
    cl = [hl[0] - numofiterations, hl[1]]
    plt.plot(cl[0], cl[1], color="blue", marker='o')
    # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')
    hl = cl
    for y in range (int(numofiterations)):
        cl = [hl[0]+z, hl[1]]
        plt.plot(cl[0], cl[1], color="blue", marker='o')
        # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')
        hl = cl
    cl = [hl[0] + numofiterations, hl[1]]
    plt.plot(cl[0], cl[1], color="blue", marker='o')
    # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')

    hl = cl
    for a in range (int(numofiterations)):
        cl = [hl[0]-z, hl[1]]
        plt.plot(cl[0], cl[1], color="blue", marker='o')
        # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')
        hl = cl

hl = [0,0]
for b in range (1, (radius)+1):
    cl = [hl[0], hl[1]-z]
    plt.plot(cl[0], cl[1], color="blue", marker='o')
    # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')

    hl = cl
    chordlength = math.sqrt((radius)**2 - (b)**2)
    print(chordlength)
    numofiterations = chordlength // z
    cl = [hl[0] - numofiterations, hl[1]]
    plt.plot(cl[0], cl[1], color="blue", marker='o')
    # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')

    hl = cl
    for y in range (int(numofiterations)):
        cl = [hl[0]+z, hl[1]]
        plt.plot(cl[0], cl[1], color="blue", marker='o')
        # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')

        hl = cl
    cl = [hl[0] + numofiterations, hl[1]]
    plt.plot(cl[0], cl[1], color="blue", marker='o')
    # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')

    hl = cl
    for a in range (int(numofiterations)):
        cl = [hl[0]-z, hl[1]]
        plt.plot(cl[0], cl[1], color="blue", marker='o')
        # plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')

        hl = cl


    




plt.show() 