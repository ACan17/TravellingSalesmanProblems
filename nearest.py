import numpy as np

TT= np.array([[0, 28, 54, 25, 24, 83, 26],
	[28,0,34,8,50,66,10],
	[54,34,0,30,66,31,28],
	[25,8,30,0,45,62,2],
    [24,50,66,45,0,90,45],
    [83,66,31,62,90,0,59],
    [26,10,28,2,45,59,0]])

# assume we start in node 0
currentStop = 0
routeList = [0]
for _i in range(len(TT)-1):
    TT[:,currentStop] = 50 # Set column of visited stop to very large number
    currentStop = np.argmin(TT[currentStop,:])
    routeList.append(currentStop)

print("Path Taken:", routeList, "Total Distance:", np.sum(TT[routeList[:-1],routeList[1:]]))