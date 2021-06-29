import numpy as np
import math
import random
import matplotlib.pyplot as plt
import time

# Choose up to k points around each reference point as candidates for a new
# sample point
#outside of small modification the code between these asterisks came from #https://scipython.com/blog/poisson-disc-sampling-in-python/
#****
k = 3

# Minimum distance between samples
r = 2

width, height = 60, 45

# Cell side length
a = r/np.sqrt(2)
# Number of cells in the x- and y-directions of the grid
nx, ny = int(width / a) + 1, int(height / a) + 1

# A list of coordinates in the grid of cells
coords_list = [(ix, iy) for ix in range(nx) for iy in range(ny)]
# Initilalize the dictionary of cells: each key is a cell's coordinates, the
# corresponding value is the index of that cell's point's coordinates in the
# samples list (or None if the cell is empty).
cells = {coords: None for coords in coords_list}

def get_cell_coords(pt):
    """Get the coordinates of the cell that pt = (x,y) falls in."""

    return int(pt[0] // a), int(pt[1] // a)

def get_neighbours(coords):
    """Return the indexes of points in cells neighbouring cell at coords.

    For the cell at coords = (x,y), return the indexes of points in the cells
    with neighbouring coordinates illustrated below: ie those cells that could
    contain points closer than r.

                                     ooo
                                    ooooo
                                    ooXoo
                                    ooooo
                                     ooo

    """

    dxdy = [(-1,-2),(0,-2),(1,-2),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),
            (-2,0),(-1,0),(1,0),(2,0),(-2,1),(-1,1),(0,1),(1,1),(2,1),
            (-1,2),(0,2),(1,2),(0,0)]
    neighbours = []
    for dx, dy in dxdy:
        neighbour_coords = coords[0] + dx, coords[1] + dy
        if not (0 <= neighbour_coords[0] < nx and
                0 <= neighbour_coords[1] < ny):
            # We're off the grid: no neighbours here.
            continue
        neighbour_cell = cells[neighbour_coords]
        if neighbour_cell is not None:
            # This cell is occupied: store this index of the contained point.
            neighbours.append(neighbour_cell)
    return neighbours

def point_valid(pt,Rad):
    """Is pt a valid point to emit as a sample?

    It must be no closer than r from any other point: check the cells in its
    imme iate neighbourhood.

    """

    cell_coords = get_cell_coords(pt)
    for idx in get_neighbours(cell_coords):
        nearby_pt = samples[idx]
        # Squared distance between or candidate point, pt, and this nearby_pt.
        distance2 = (nearby_pt[0]-pt[0])**2 + (nearby_pt[1]-pt[1])**2
        if distance2 < Rad**2:
            # The points are too close, so pt is not a candidate.
            return False
    # All points tested: if we're here, pt is valid
    return True

def get_point(k, refpt, Rad):
    """Try to find a candidate point relative to refpt to emit in the sample.

    We draw up to k points from the annulus of inner radius r, outer radius 2r
    around the reference point, refpt. If none of them are suitable (because
    they're too close to existing points in the sample), return False.
    Otherwise, return the pt.

    """
    i = 0
    while i < k:
        rho, theta = np.random.uniform(r, 2*r), np.random.uniform(0, 2*np.pi)
        pt = refpt[0] + rho*np.cos(theta), refpt[1] + rho*np.sin(theta)
        if not (0 <= pt[0] < width and 0 <= pt[1] < height):
            # This point falls outside the domain, so try again.
            continue
        if point_valid(pt,Rad):
            return pt
        i += 1
    # We failed to find a suitable point in the vicinity of refpt.
    return False

# Pick a random point to start with.
pt = (np.random.uniform(0, width), np.random.uniform(0, height))
samples = [pt]
# Our first sample is indexed at 0 in the samples list...
cells[get_cell_coords(pt)] = 0
# ... and it is active, in the sense that we're going to look for more points
# in its neighbourhood.
active = [0]

nsamples = 1
# As long as there are points in the active list, keep trying to find samples.
while active:
    # choose a random "reference" point from the active list.
    idx = np.random.choice(active)
    refpt = samples[idx]
    # Try to pick a new point relative to the reference point.
    pt = get_point(k, refpt, r)
    if pt:
        # Point pt is valid: add it to the samples list and mark it as active
        samples.append(pt)
        nsamples += 1
        active.append(len(samples)-1)
        cells[get_cell_coords(pt)] = len(samples) - 1
    else:
        # We had to give up looking for valid points near refpt, so remove it
        # from the list of "active" points.
        active.remove(idx)

#**
#prints circle centers for observation and bug testing
print(samples)
#randomly choose a circle center store it as start and remove it from the samples list, do the same but wi
start = random.choice(samples)

samples.remove(start)
end = random.choice(samples)
samples.remove(end)

startpt = start

endpt = end
print("end: "+str(endpt))
print("start: "+str(startpt))
#samples is output for sampling
def plot():
    figure, axes = plt.subplots()
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.axis('off')
    for i in samples:
        C=plt.Circle(i,radius=1)
        axes.add_artist(C)
plot()
plt.scatter([startpt[0],endpt[0]], [startpt[1],endpt[1]],s=1, marker='o', color='tomato', label='point')
plt.show()

#Navigation, there are definitly faster ways to do this but this is just a basic thing
def distfuncpar(pt1,pt2):
    return((((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)))
def nearestobject(pt):
    distlist = []
    for i in samples:
        ndist = distfuncpar(i,pt)
        distlist.append(ndist)
    distlist.append(pt[1]+1)
    distlist.append(width-pt[0]+1)
    distlist.append(pt[0]+1)
    distlist.append(height-pt[1]+1)
    discan = np.amin(distlist)
    return((np.sqrt(np.abs(discan))))
def raymarch(point,theta):
    intersect = False
    while intersect != True:
        size=nearestobject(point)-1
        point = (point[0] + size*np.cos(theta), point[1] + size*np.sin(theta))
        if size <.00001:
            intersect = True
        if math.isnan(size) == True:
            intersect = True
    return(point)

cur_point = startpt
while True:
    vaild = False
    theta = input("input theta: ")
    if theta == 'quit':
        break
    theta = float(theta)
    coll_point = raymarch(cur_point,theta)
    plot()
    plt.plot([coll_point[0],cur_point[0]],[coll_point[1],cur_point[1]], color='r')
    plt.scatter([cur_point[0]], [cur_point[1]],s=3, marker='o', color='orange', label='point')
    plt.scatter([coll_point[0]], [coll_point[1]],s=3, marker='o', color='g', label='point')
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.axis('off')
    plt.show()
    dis = np.sqrt(distfuncpar(cur_point,coll_point))
    while vaild != True:
        vaild = True
        movdis =  float(input("input distance between 0 and " + str(dis) +": " ))
        if movdis < 0:
            vaild = False
            print("not within bounds")
        if movdis > dis:
            vaild = False
            print("not within bounds")
    cur_point = (cur_point[0] + movdis*np.cos(theta), cur_point[1] + movdis*np.sin(theta))
    plot()
    plt.scatter([cur_point[0]], [cur_point[1]],s=3, marker='o', color='r', label='point')
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.axis('off')
    plt.show()
print(cur_point)


nearestobject(startpt)


