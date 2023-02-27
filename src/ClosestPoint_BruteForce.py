import Helper

def ClosestPoint_Bf(nDim, points, maxRange, minRange):
    totalOps = 0
    minDist = (maxRange-minRange)*nDim
    dist = [[0 for i in range(len(points))] for j in range(len(points))]
    closestIdx = []
    for i in range(0, len(points) - 1):
        for j in range(i + 1, len(points)):
            dist[i][j] = Helper.EucDist(nDim, points[i], points[j])
            if(dist[i][j] < minDist):
                minDist = dist[i][j]
            totalOps += 1
    for i in range(0, len(points) - 1):
        for j in range(i + 1, len(points)):
            if(dist[i][j] == minDist):
                closestIdx.append((i, j))
    return minDist, closestIdx, totalOps

