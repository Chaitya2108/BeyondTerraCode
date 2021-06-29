import matplotlib.pyplot as plt
import math
from time import sleep

allthepoints = []

home_location = [0, 0]

z = 1

point2 = [0, 10]

point3 = [10, 10]

point4 = [10, 0]

maximum = 10
minimum = 0

plt.plot(home_location[0], home_location[1], color="blue", marker = "o")
plt.title("Points")
plt.xlabel("x")
plt.ylabel("y")

distance = 10

cp = home_location
allthepoints.append(cp)
print(cp)

for x in range(distance//2):
    for y in range(distance):
        newpoint_x = cp[0]
        newpoint_y = cp[1] + z
        sleep(1)
        plt.plot(newpoint_x, newpoint_y, color="blue", marker="o")
        plt.plot([cp[0], newpoint_x], [cp[1], newpoint_y], "r")
        cp = [newpoint_x, newpoint_y]
    newpoint_x = cp[0] + z
    newpoint_y = cp[1]
    sleep(1)
    plt.plot(newpoint_x, newpoint_y, color="blue", marker = "o")
    plt.plot([cp[0], newpoint_x], [cp[1], newpoint_y], 'r')
    cp = [newpoint_x, newpoint_y]

    for y in range(distance):
        newpoint_x = cp[0]
        newpoint_y = cp[1] - z
        sleep(1)
        plt.plot(newpoint_x, newpoint_y, color="blue", marker="o")
        plt.plot([cp[0], newpoint_x], [cp[1], newpoint_y], "r")
        cp = [newpoint_x, newpoint_y]
    newpoint_x = cp[0] + z
    newpoint_y = cp[1]
    sleep(1)
    plt.plot(newpoint_x, newpoint_y, color="blue", marker = "o")
    plt.plot([cp[0], newpoint_x], [cp[1], newpoint_y], 'r')
    cp = [newpoint_x, newpoint_y]

for y in range(distance):
    newpoint_x = cp[0]
    newpoint_y = cp[1] + z
    sleep(1)
    plt.plot(newpoint_x, newpoint_y, color="blue", marker="o")
    plt.plot([cp[0], newpoint_x], [cp[1], newpoint_y], "r")
    cp = [newpoint_x, newpoint_y]
    
length = len(allthepoints)
print(length)

# for i in range(length):
#     for j in range(1, length+1):
#         try:
#             x_co = [allthepoints[i][0], allthepoints[j][0]]
#             y_co = [allthepoints[i][1], allthepoints[j][1]]
#             plt.plot(x_co, y_co)
#             x_co = []
#             y_co = []
#         except IndexError:
#             break



print(allthepoints)
plt.show()



