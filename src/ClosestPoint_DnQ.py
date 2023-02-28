import Helper
import ClosestPoint_BruteForce

# ALGORITMA UTAMA
# closestPair, untuk 2 sumbu
def closestPair(Ndim, Points, N, totalOps):                       # ambil koordinat x, tentukan panjang lebar x yang mungkin
    if (N <= 3):
        d, Pair, totalOps = ClosestPoint_BruteForce.ClosestPoint_Bf(Ndim, Points)
        return d, Pair, totalOps
    else:
        S1,S2 = Helper.split(Points)                 # bagi menjadi 2
        d1, Pair1, totalOps1 = closestPair(Ndim, S1, len(S1), totalOps)
        d2, Pair2, totalOps2 = closestPair(Ndim, S2, len(S2), totalOps)
        totalOps += totalOps1 + totalOps2 

        if(d1 == d2):
            d = d1
            Pair = Pair1 + Pair2
        elif (d1 < d2):
            d = d1
            Pair = Pair1
        elif (d2 < d1):
            d = d2
            Pair = Pair2

        batasx = S1[len(S1)-1][0] + (S1[len(S1)-1][0] + S2[0][0])/2
        temp = []

        i = len(S1)-1
        while (i >= 0 and S1[i][0] >= batasx - d):
            if (S1[i] not in temp):
                temp.append(S1[i])
            i = i - 1
        
        i = 0
        while (i < len(S2) and S2[i][0] <= batasx + d):
            if (S2[i] not in temp):
                temp.append(S2[i])
            i = i + 1

        if (len(temp) > 1):
            for i in range(len(temp)):
                for j in range(i + 1, len(temp)):
                    if (temp[i] != temp[j]):
                        check = True
                        k = 0
                        while(check and k < Ndim):
                            if(abs(temp[i][k] - temp[j][k]) > d):
                                check = False
                            k = k + 1
                        
                        if (check):
                            if(Helper.EucDist(Ndim,temp[i], temp[j]) < d):
                                totalOps += 1
                                d = Helper.EucDist(Ndim,temp[i], temp[j])
                                Pair = [(temp[i], temp[j])]
                            elif(Helper.EucDist(Ndim,temp[i], temp[j]) == d):
                                Pair.append((temp[i], temp[j])) 
        return d, Pair, totalOps