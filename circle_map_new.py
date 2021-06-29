import numpy as np 
import matplotlib.pyplot as plt 
import math
 
angle = np.linspace( 0 , 2 * np.pi , 150 ) 
 
radius = int(input("Enter the radius: "))
hl = [0,]
 
x = radius * np.cos( angle ) 
y = radius * np.sin( angle ) 
 
figure, axes = plt.subplots( 1 ) 
 
axes.plot( x, y ) 
axes.set_aspect( 1 ) 
 
plt.title( 'Parametric Equation Circle' ) 

z = int(input("Enter the radius: "))

hl.append(radius)
print(hl)


counter = 1
plt.plot(hl[0], hl[1], color="blue", marker="o")
# for x in range (1, (radius * 2)+1, z):
for x in range(0, (radius*2)+1, z):
    print(x)
    chordlength = math.sqrt(radius**2 - (radius-(x))**2)
    numofiterations = (chordlength*2) // z
    if counter % 2 != 0:
        cl = [chordlength, radius-(x)]
        plt.plot(cl[0], cl[1], color="blue", marker="o")
        plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')
        hl = cl
        for y in range (int(numofiterations)):
            cl = [hl[0]-z, hl[1]]
            plt.plot(cl[0], cl[1], color="blue", marker="o")
            plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')
            hl = cl
    else:
        cl = [-1*chordlength, radius-(x)]
        plt.plot(cl[0], cl[1], color="blue", marker="o")
        plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')
        hl = cl
        for y in range (int(numofiterations)):
            cl = [hl[0]+z, hl[1]]
            plt.plot(cl[0], cl[1], color="blue", marker="o")
            plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')
            hl = cl
    counter += 1
# cl = [0, -1*radius]
# plt.plot(cl[0], cl[1], color="blue", marker="o")
# plt.plot([hl[0], cl[0]], [hl[1], cl[1]], 'r')
# hl = cl


plt.show() 