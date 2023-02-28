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
def closestPair(Points,N):                       # ambil koordinat x, tentukan panjang lebar x yang mungkin
    if (N <= 3):
        if (len(Points) == 1):
            return None, None
        else:
            S = Helper.sortAxis(Points,0)
            print(len(S))
            d = Helper.EucDist(3,Points[0], Points[1])
            Pair = [Points[0],Points[1]]
            return d, Pair
    else:
        d = None
        Pair = None
        S = Helper.sortAxis(Points,0)
        S1,S2 = split(S)                 # bagi menjadi 2
        S1 = Helper.sortAxis(S1,1)
        S2 = Helper.sortAxis(S2,1)
        SS1,SS2 = split(S1)                   # bagi menjadi 4
        SS3,SS4 = split(S2)

        print(SS1)
        print(SS2)
        print(SS3)
        print(SS4)

        d1, Pair1 = closestPair(SS1,len(SS1))
        d2, Pair2 = closestPair(SS2,len(SS2))
        d3, Pair3 = closestPair(SS3,len(SS3))
        d4, Pair4 = closestPair(SS4,len(SS4))
        
        if (d1 is not None and d2 is not None and d3 is not None and d4 is not None):
            if (d1 == min(d1,d2,d3,d4)):
                d = d1
                Pair = Pair1
            elif (d2 == min(d1,d2,d3,d4)):
                d = d2
                Pair = Pair2
            elif (d3 == min(d1,d2,d3,d4)):
                d = d3
                Pair = Pair3
            elif (d4 == min(d1,d2,d3,d4)):
                d = d4
                Pair = Pair4

        batasx = S1[len(S1)-1][0] + (S1[len(S1)-1][0] + S2[0][0])/2
        batasy = S1[len(S1)-1][1] + (S1[len(S1)-1][1] + S2[0][1])/2
        temp = []

        i = len(SS1)-1
        while (i >= 0 and ((d is None) or (SS1[i][0] > batasx - d and SS1[i][1] > batasy - d))):
            if (SS1[i] not in temp):
                temp.append(SS1[i])
            i = i - 1

        i = len(SS2)-1
        while (i >=0 and ((d is None) or (SS2[i][0] > batasx - d and SS2[i][1] < batasy + d))):
            if (SS2[i] not in temp):
                temp.append(SS2[i])
            i = i - 1

        i = 0
        while (i < len(SS3) and ((d is None) or (SS3[i][0] < batasx - d and SS3[i][1] > batasy - d))):
            if (SS3[i] not in temp):
                temp.append(SS3[i])
            i = i + 1

        i = 0
        while (i < len(SS4) and ((d is None) or (SS2[i][0] > batasx - d and SS2[i][1] < batasy + d))):
            if (SS4[i] not in temp):
                temp.append(SS4[i])
            i = i + 1

        print(temp)

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
                            if(d is None or Helper.EucDist(3,temp[i], temp[j]) < d):
                                d = Helper.EucDist(3,temp[i], temp[j])
                                Pair = [temp[i], temp[j]]
        return d, Pair


points = [[1,2,3],[7,6,7],[8,9,10],[11,2,4],[12,3,2],[15,15,12]]
jumlahPerhitungan = 0

d, Pair = closestPair(points,6)
print(d)
print(Pair)