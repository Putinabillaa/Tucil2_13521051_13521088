def jarak(A,B):
    sum2 = 0
    for i in range(len(A)):
        sum2 = (A[i] - B[i])**2
    d = (sum2)**1/2
    return d

def addPair(A,B):
    Pair.append([[A],[B]])

def split(P,N):
    P1 = []
    P2 = []
    for i in range(int(N/2)):
        P1.append(P[i])
    for j in range(i,N):
        P2.append(P[i])
    return P1,P2

def printPair(pair):
    for i in range(len(pair)):
        print(pair[i])

# ALGORITMA UTAMA
def closestPair(Points,N):                       # ambil koordinat x, tentukan panjang lebar x yang mungkin
    if (N == 2):
        d = jarak(Points[0], Points[1])
        Pair = [Points[0],Points[1]]
        return d, Pair
    else:
        S1,S2 = split(Points,N)               # bagi menjadi 2
        d1, Pair1 = closestPair(S1,int(N/2))
        d2, Pair2 = closestPair(S2,int(N/2))

        if (d1 < d2):
            d = d1
            Pair = Pair1
        else:
            d = d2
            Pair = Pair2
        
        batas = S1[len(S1)-1][0] + (S1[len(S1)-1][0] + S2[0][0])/2        
        temp = []

        # cari di kiri
        i = len(S1)-1
        while (S1[i][0] > batas - d):
            temp.append(S1[i][0])
            i = i - 1
        # cari di kanan
        i = 0
        while (S2[i][0] < batas + d):
            temp.append(S2[i][0])
            i = i + 1

        # proses himpunan strip
        for i in range(len(temp)):
            for j in range(len(temp)):
                check = True
                k = 0
                while(check and k < 2):
                    if(abs(temp[i][k] - temp[j][k]) > d):
                        check = False
                
                if (check):
                    if(jarak(temp[i], temp[j]) < d):
                        d = jarak(temp[i], temp[j])
                        Pair = [temp[i], temp[j]]

        return d, Pair
    
# ALGORITMA UTAMA

# N = int(input("Masukkan dimensi: "))
points = [[1,2,3],[3,4,5],[7,6,7],[8,9,10]]
jumlahPerhitungan = 0

d, Pair = closestPair(points,4)
printPair(d)
printPair(Pair)