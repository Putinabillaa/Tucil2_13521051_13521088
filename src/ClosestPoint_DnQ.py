import Helper

def split(P):
    P1 = []
    P2 = []
    for i in range(int(len(P)/2)):
        P1.append(P[i])
    for j in range(int(len(P)/2),len(P)):
        P2.append(P[j])
    return P1,P2

# ALGORITMA UTAMA
# closestPair, untuk 2 sumbu
def closestPair(Ndim, Points, N, totalOps):                       # ambil koordinat x, tentukan panjang lebar x yang mungkin
    if (N <= 3):
        if (len(Points) == 1):
            return None, None, 0
        elif (len(Points) == 2):
            S = Helper.sortAxis(Points,0)
            totalOps += 1
            d = Helper.EucDist(Ndim, Points[0], Points[1])
            Pair = [Points[0],Points[1]]
            return d, Pair, totalOps
        else:
            S = Helper.sortAxis(Points,0)
            totalOps += 3
            d1 = Helper.EucDist(Ndim, Points[0], Points[1])
            d2 = Helper.EucDist(Ndim, Points[1], Points[2])
            d3 = Helper.EucDist(Ndim, Points[0], Points[2])
            if (d1 == min(d1,d2,d3)):
                d = d1
                Pair = [Points[0], Points[1]]
            elif (d2 == min(d1,d2,d3)):
                d = d2
                Pair = [Points[1], Points[2]]
            elif (d3 == min(d1,d2,d3)):
                d = d3
                Pair = [Points[0], Points[2]]
            return d, Pair, totalOps
    else:
        d = None
        Pair = None
        S = Helper.sortAxis(Points,0)
        S1,S2 = split(S)                 # bagi menjadi 2
        # S1 = Helper.sortAxis(S1,1)
        # S2 = Helper.sortAxis(S2,1)
        # SS1,SS2 = split(S1)                   # bagi menjadi 4
        # SS3,SS4 = split(S2)

        # d1, Pair1, totalOps1 = closestPair(Ndim, SS1, len(SS1), totalOps)
        # d2, Pair2, totalOps2 = closestPair(Ndim, SS2, len(SS2), totalOps)
        # d3, Pair3, totalOps3 = closestPair(Ndim, SS3, len(SS3), totalOps)
        # d4, Pair4, totalOps4 = closestPair(Ndim, SS4, len(SS4), totalOps)
        d1, Pair1, totalOps1 = closestPair(Ndim, S1, len(S1), totalOps)
        d2, Pair2, totalOps2 = closestPair(Ndim, S2, len(S2), totalOps)
        totalOps += totalOps1 + totalOps2

        # notNone = []
        # if (d1 is not None):
        #     notNone.append(d1)
        # if (d2 is not None):
        #     notNone.append(d2)
        # if (d3 is not None):
        #     notNone.append(d3)
        # if (d4 is not None):
        #     notNone.append(d4)
            
        # if (d1 is not None and d1 == min(notNone)):
        #     d = d1
        #     Pair = Pair1
        # elif (d2 is not None and d2 == min(notNone)):
        #     d = d2
        #     Pair = Pair2
        # elif (d3 is not None and d3 == min(notNone)):
        #     d = d3
        #     Pair = Pair3
        # elif (d4 is not None and d4 == min(notNone)):
        #     d = d4
        #     Pair = Pair4

        if (d1 == min(d1,d2)):
            d = d1
            Pair = Pair1
        else:
            d = d2
            Pair = Pair2

        batasx = S1[len(S1)-1][0] + (S1[len(S1)-1][0] + S2[0][0])/2
        # batasy = S1[len(S1)-1][1] + (S1[len(S1)-1][1] + S2[0][1])/2
        temp = []

        i = len(S1)-1
        while (i >= 0 and ((d1 is None) or (d is not None and S1[i][0] > batasx - d ))):
            if (S1[i] not in temp):
                temp.append(S1[i])
            i = i - 1
        
        i = 0
        while (i < len(S2) and ((d2 is None) or (d is not None and S2[i][0] < batasx + d))):
            if (S2[i] not in temp):
                temp.append(S2[i])
            i = i + 1

        # i = len(SS1)-1
        # while (i >= 0 and ((d1 is None) or (d is not None and SS1[i][0] > batasx - d and SS1[i][1] > batasy - d))):
        #     if (SS1[i] not in temp):
        #         temp.append(SS1[i])
        #     i = i - 1

        # i = len(SS2)-1
        # while (i >=0 and ((d2 is None) or (d is not None and SS2[i][0] > batasx - d and SS2[i][1] < batasy + d))):
        #     if (SS2[i] not in temp):
        #         temp.append(SS2[i])
        #     i = i - 1

        # i = 0
        # while (i < len(SS3) and ((d3 is None) or (d is not None and SS3[i][0] < batasx + d and SS3[i][1] > batasy - d))):
        #     if (SS3[i] not in temp):
        #         temp.append(SS3[i])
        #     i = i + 1

        # i = 0
        # while (i < len(SS4) and ((d4 is None) or (d is not None and SS4[i][0] < batasx + d and SS4[i][1] < batasy + d))):
        #     if (SS4[i] not in temp):
        #         temp.append(SS4[i])
        #     i = i + 1

        # proses himpunan strip
        if (len(temp) > 1):
            for i in range(len(temp)):
                for j in range(i + 1, len(temp)):
                    if (temp[i] != temp[j]):
                        check = True
                        k = 0
                        while(check and k < 3):
                            if(d is not None and abs(temp[i][k] - temp[j][k]) > d):
                                check = False
                            k = k + 1
                        
                        if (check):
                            if(d is None or Helper.EucDist(Ndim,temp[i], temp[j]) < d):
                                totalOps += 1
                                d = Helper.EucDist(Ndim,temp[i], temp[j])
                                Pair = [temp[i], temp[j]]
        return d, Pair, totalOps