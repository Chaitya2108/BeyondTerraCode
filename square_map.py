import matplotlib.pyplot as plt
import math
point1 = [1, 1]
point2 = [2, 1]

newpoints = []

distance = math.sqrt((point2[1] - point1[1])^2 + (point2[0] - point1[0])^2)
if distance > 0.2:
    print(distance)
    numofpoints = distance / 0.2
    for x in range(1, int(numofpoints)+1):
        addpoint = newpoints.append([point1[0]+0.2*x, point1[1]])
    print(newpoints)

plt.plot(point1[0],point1[1], color="blue", marker = "o")
plt.title("Points")
plt.xlabel("x")
plt.ylabel("y")
for y in range (len(newpoints)):
    plt.plot(newpoints[y][0], newpoints[y][1], color="blue", marker="o")

point3 = [2, 2]
point2 = [2, 1]

newpoints_1 = []

distance_1 = math.sqrt((point3[1] - point2[1])**2 + (point3[0] - point2[0])**2)
if distance_1 > 0.2:
    print(distance_1)
    numofpoints_1 = distance_1 / 0.2
    for x_1 in range(1, int(numofpoints_1)+1):
        addpoint_1 = newpoints_1.append([point2[0], point2[1]+0.2*x_1])
    print(newpoints_1)

plt.plot(point2[0],point2[1], color="blue", marker = "o")
for y_1 in range (len(newpoints_1)):
    plt.plot(newpoints_1[y_1][0], newpoints_1[y_1][1], color="blue", marker="o")

point4 = [1, 2]
point3 = [2, 2]

newpoints_2 = []

distance_2 = math.sqrt((point4[1] - point3[1])**2 + (point4[0] - point3[0])**2)
if distance_2 > 0.2:
    print(distance_2)
    numofpoints_2 = distance_2 / 0.2
    for x_2 in range(1, int(numofpoints_2)+1):
        addpoint_2 = newpoints_2.append([point3[0]-0.2*x_2, point3[1]])
    print(newpoints_2)

plt.plot(point3[0],point3[1], color="blue", marker = "o")
for y_2 in range (len(newpoints_2)):
    plt.plot(newpoints_2[y_2][0], newpoints_2[y_2][1], color="blue", marker="o")

point1 = [1, 1]
point4 = [1, 2]

newpoints_3 = []

distance_3 = math.sqrt((point1[1] - point4[1])**2 + (point1[0] - point4[0])**2)
if distance_3 > 0.2:
    print(distance_3)
    numofpoints_3 = distance_3 / 0.2
    for x_3 in range(1, int(numofpoints_3)+1):
        addpoint_3 = newpoints_3.append([point4[0], point4[1]-0.2*x_3])
    print(newpoints_3)

# plt.plot(point3[0],point3[1], color="blue", marker = "o")
for y_3 in range (len(newpoints_3)):
    plt.plot(newpoints_3[y_3][0], newpoints_3[y_3][1], color="blue", marker="o")

currentpoint = [1, 1]
for a in range(1, int(numofpoints)+1):
    currentpoint = [currentpoint[0]+0.2*a, currentpoint[1]]
    plt.plot(currentpoint[0], currentpoint[1], color="blue", marker="o")
    for b in range(1, int(numofpoints)+1):
        currentpoint= [currentpoint[0], currentpoint[1]+0.2*b]
        plt.plot(currentpoint[0], currentpoint[1], color="blue", marker="o")

plt.show()
