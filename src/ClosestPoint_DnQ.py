N = int(input("Masukkan dimensi: "))
jumlahPerhitungan = 0
Pair = []

def jarak(A,B):
    sum2 = 0
    for i in range(N):
        sum2 = (A[i] - B[i])**2
    d = (sum)**1/2
    return d

def addPair(A,B):
    Pair.append([A],[B])

def split(P,i,f):
    batas = i + (f-i)/2
    P1 = []
    P2 = []
    for i in range(len(P)):
        if (P[i][0] < batas):
            P1.append(P[i])
        else:
            P2.append(P[i])
    return P1,P2


# ALGORITMA UTAMA
def closestPair(Points,N):
    xi = Points[0][0]
    xf = Points[N-1][0]                           # ambil koordinat x, tentukan panjang lebar x yang mungkin
    if (N == 2):
        d = jarak(Points[0], Points[1])
        addPair(Points[0],Points[1])
        return d
    else:
        S1,S2 = split(Points,xi,xf)               # bagi menjadi 2
        d1 = closestPair(S1,N/2)
        d2 = closestPair(S2,N/2)
        d = min(d1,d2)
        
        pleft = S1[len(S1)-1]
        pright = S2[0]

        if (jarak(pleft,pright) < d):
            d = jarak(pleft,pright)
        
        return d
    
# belum kelar:(