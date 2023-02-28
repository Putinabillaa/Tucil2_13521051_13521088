from math import sqrt
import random
import matplotlib.pyplot as plt

'''
Method untuk men-generate list points dalam R^nDim
dengan koordinat random dalam rentang minRange-maxRange
'''
def ListRandomizer(nDim, n, maxRange, minRange):
    points = [[0 for i in range(nDim)] for j in range(n)]
    for i in range(0, n):
        for j in range (0, nDim):
            points[i][j] = random.uniform(minRange, maxRange)
    return points

'''
Method untuk menghitung jarak euclidian antara
2 titik dalam R^nDim
'''
def EucDist(nDim, p1, p2):
    sum = 0
    for i in range(0, nDim):
        sum += pow((p2[i] - p1[i]), 2)
    return sqrt(sum)

'''
Method untuk mengurutkan koordinat berdasarkan sumbunya
i = 0 --> sumbu x
i = 1 --> sumbu y
dst.
'''
def sortAxis(points,i):
    for j in range(len(points)):
        min = j
        for k in range(j+1,len(points)):
            if (points[k][i] < points[min][i]):
                min = k
        points[j], points[min] = points[min], points[j]
    return points

'''
Method membagi array menjadi 2 bagian
'''
def split(P):
    P1 = []
    P2 = []
    for i in range(int(len(P)/2)):
        P1.append(P[i])
    for j in range(int(len(P)/2),len(P)):
        P2.append(P[j])
    return P1,P2

'''
Method untuk membaca file berisi koordinat titik
'''
def ReadFile(nDim, n, maxRange, minRange):
    filePath = input("Enter your file path: ") 
    f = open(filePath, 'r')
    points = [[0 for i in range(nDim)] for j in range(n)]
    i = 0
    for line in f:
        # format koordinat titik: Coordinate^1, Coordinate^2, ..., Coordinate^nDim \n
        try:
            points[i] = [float(j) for j in line.split(",")]
        except IndexError:
            print("ERROR! Please input with a correct number of dimensions and points")
            return -1
        for j in range (0, nDim):
            if (points[i][j] > maxRange or points[i][j] < minRange): 
                print("ERROR! Your points in \'" + str(filePath) + "\' contain coordinates that exceed the range limit")
                print("Please input coordinates in between " + str(minRange) + " and " + str(maxRange))
                return -1
        i += 1
    f.close
    return points

'''
Method untuk memvisualisasikan titik-titik 2D dalam 
bentuk scatter plot, untuk pasangan titik-titik terdekat 
diberi warna berbeda (tidak hitam)
'''
def Visualizer3D(n, points, Pair):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    getColors = lambda x: ["#%06x" % random.randint(100, 0xFFFFFF) for i in range(x)]
    colors = getColors(n)
    for i in range(0, n):
        ax.scatter(points[i][0], points[i][1], points[i][2], color='black', marker='o')
        for j in range (0, len(Pair)):
            if((points[i][0] == Pair[j][0][0] and points[i][1] == Pair[j][0][1] and points[i][2] == Pair[j][0][2]) or 
            (points[i][0] == Pair[j][1][0] and points[i][1] == Pair[j][1][1] and points[i][2] == Pair[j][1][2])): 
                ax.scatter(points[i][0], points[i][1], points[i][2], color=colors[j], marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

'''
Method untuk memvisualisasikan titik-titik 2D dalam 
bentuk scatter plot, untuk pasangan titik-titik terdekat 
diberi warna berbeda (tidak hitam)
'''
def Visualizer2D(n, points, Pair):
    getColors = lambda x: ["#%06x" % random.randint(100, 0xFFFFFF) for i in range(x)]
    colors = getColors(n)
    for i in range(0, n):
        plt.scatter(points[i][0], points[i][1], color='black', marker='o')
        for j in range (0, len(Pair)):
            if((points[i][0] == Pair[j][0][0] and points[i][1] == Pair[j][0][1]) or 
            (points[i][0] == Pair[j][1][0] and points[i][1] == Pair[j][1][1])): 
                plt.scatter(points[i][0], points[i][1], color=colors[j], marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

'''
Method untuk menampilkan splash screen
'''
def SplashScreen():
    print("-------------------")
    print("  Closest Points!  ")
    print("-------------------")