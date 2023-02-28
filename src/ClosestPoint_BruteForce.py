import Helper

def ClosestPoint_Bf(nDim, points):
    totalOps = 0
    minDist = Helper.EucDist(nDim, points[0], points[1])
    Pair = []
    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            dist = Helper.EucDist(nDim, points[i], points[j])
            if(dist < minDist):
                minDist = dist
                Pair = [(points[i], points[j])]
            elif(dist == minDist):
                Pair.append((points[i], points[j]))
            totalOps += 1
    return minDist, Pair, totalOps