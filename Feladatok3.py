import numpy as np

def feladat_1():
    n=int(input("Hány darab szám? "))
    t=np.empty(n,int)
    for i in range(n):
        a=int(input())
        t[i]=a
    for i in range(0,n-1):
        if t[i]==t[i+1] or t[i]==t[i-1]:
            print(i)

def feladat_2():
    n=int(input("Hány darab szám? "))
    paros=0
    paratlan=0
    for i in range(n):
        a=int(input())
        if a%2==0:
            paros+=1
        else:
            paratlan+=1
    return paros/paratlan


def feladat_3():
    n = int(input("Hány darab szám? "))
    s=0
    t=np.empty(n,float)
    for i in range(n):
        a=float(input())
        t[i]=abs(a)
        s=s+abs(a)
    return s/n

def feladat_4():
    n=int(input("Hány darab szám? "))
    szorzat=1
    negativ_osszeg=0
    negativ_db=0
    for i in range(n):
        a=float(input())
        if a>0:
            szorzat=szorzat*a
        elif a<0:
            negativ_osszeg=negativ_osszeg+a
            negativ_db+=1
    return szorzat,negativ_osszeg/negativ_db

def feladat_5():
    n=int(input("Hány darab szám? "))
    t=np.empty(n,int)
    szorzat=1
    osszeg=0
    for i in range(n):
        t[i]=int(input())
    for k in t:
        if k<7:
            szorzat=szorzat*k
        elif k>10:
            osszeg+=k
    return szorzat,osszeg

def feladat_6():
    strazsa=True
    k=0
    elozo = 0
    elozo_elotti = 0
    while strazsa:
        k=k+1
        aktualis=int(input())
        if aktualis==0:
            strazsa=False
        elif elozo+elozo_elotti==aktualis:
            print(aktualis)
        elif k==1:
            elozo=aktualis
        else:
            elozo_elotti=elozo
            elozo=aktualis

def feladat_7():
    li=[]
    strazsa=True
    while strazsa:
        a=int(input())
        if a==0:
            strazsa=False
        else:
            li.append(a)
    a,b,c=0,0,0
    max_atlag = 0
    for i in range(0,len(li)-2):
        if ((li[i]+li[i+1]+li[i+2])/3)>max_atlag:
            a,b,c=li[i],li[i+1],li[i+2]
            max_atlag=(li[i]+li[i+1]+li[i+2])/3
    print(a,b,c)

double_tomb=np.empty(4,np.double)
double_tomb[0]=1.144234
double_tomb[1]=2
double_tomb[2]=9.214
double_tomb[3]=7
def feladat_8(double_tomb,n):
    novekvo=True
    for i in range(0,len(double_tomb)-1):
        if double_tomb[i]>double_tomb[i+1]:
            novekvo=False
    return novekvo

tomb=np.empty(5,np.int)
tomb[0]=1
tomb[1]=2
tomb[2]=9
tomb[3]=7
tomb[4]=11
def feladat_9(tomb,n):
    osztok=[]
    for i in tomb:
        for j in range(2,(i//2)+1):
            if i%j==0 and j not in osztok:
                osztok.append(j)
            elif i%j==0 and j in osztok:
                return 0
    return 1

tomb=np.empty(5,np.int)
tomb[0]=1
tomb[1]=2
tomb[2]=9
tomb[3]=7
tomb[4]=11
def feladat_10(tomb,n,k):
    for i in range(0,n-1):
        minh=i
        for j in range(i+1,n):
            if tomb[j]<tomb[minh]:
                minh=j
        tomb[i],tomb[minh]=tomb[minh],tomb[i]
    ah=0
    fh=n-1
    kozep=(ah+fh)//2
    while ah<=fh:
        osztok=2
        for i in range(2,(tomb[kozep]//2)+1):
            if tomb[kozep]+i==0:
                osztok+=1
        if osztok>k:
            return kozep
        elif osztok<k:
            ah=kozep+1
        else:
            return -1

def feladat_11():
    n=int(input("Sorok száma: "))
    m=int(input("Oszlopok száma"))
    matrix=np.empty((n,m),np.int)
    indexek=[]
    for i in range(n):
        for j in range(m):
            matrix[i][j]=int(input())
    for j in range(m):
        negativ=0
        nulla=0
        for i in range(n):
            if matrix[i][j]<0:
                negativ+=1
            elif matrix[i][j]==0:
                nulla+=1
        if negativ>=nulla*2:
            indexek.append(j)
    return indexek

matrix12=np.empty((3,2),np.int)
matrix12[0][0]=1
matrix12[0][1]=69
matrix12[1][0]=32
matrix12[1][1]=9
matrix12[2][0]=2
matrix12[2][1]=19
def feladat_12(matrix,n,m):
    eredmeny=[]
    for i in range(n):
        for j in range(m):
            if (i+j)!=0 and matrix[i][j]%(i+j)==0:
                eredmeny.append(matrix[i][j])
    return eredmeny





matrix13=np.empty((3,2),np.int)
matrix13[0][0]=2
matrix13[0][1] = 69
matrix13[1][0] = 32
matrix13[1][1] = 9
matrix13[2][0] = 1
matrix13[2][1] = 19
def feladat_13(matrix,n,m):
    matrix_uj=np.empty((n,m),np.int)
    minimumok=[]
    for j in range(m):
        minimum=matrix[j][0]
        for i in range(n):
            if matrix[i][j]<minimum:
                minimum=matrix[i][j]
        minimumok.append(minimum)
    for j in range(m):
        for i in range(n):
            matrix_uj[i][j]=matrix[i][j]-minimumok[j]
    return matrix_uj

matrix14=np.empty((3,3),np.int)
matrix14[0][0] = 1
matrix14[0][1] = 69
matrix14[0][2] = 7
matrix14[1][0] = 32
matrix14[1][1] = 0
matrix14[1][2] = 9
matrix14[2][0] = 2
matrix14[2][1] = 0
matrix14[2][2] = 3
def feladat_14(matrix,n):
    max=matrix[0][0]
    for i in range(n):
        for j in range(0,i+1):
            if matrix[i][j]>max:
                max=matrix[i][j]
    return max

matrix15 = np.empty((2, 2), np.int)
matrix15[0][0] = 1
matrix15[0][1] = 69
matrix15[1][0] = 32
matrix15[1][1] = 0
def feladat_15(matrix,n):
    valasz=True
    for i in range(n):
        if matrix[i][i]!=0:
            valasz=False
    return valasz

matrix16=np.empty((3,2),np.double)
matrix16[0][0] = 2
matrix16[0][1] = 69
matrix16[1][0] = 32
matrix16[1][1] = 9
matrix16[2][0] = 1
matrix16[2][1] = 19
transzponalt16=np.empty((2,3),np.double)
def feladat_16(matrix,n,m,transzponalt):
    for j in range(m):
        for i in range(n):
            transzponalt[j][i]=matrix[i][j]
    return transzponalt

#17-18-ik feladatot nem vettük
def main():
    feladat_1()
    print(feladat_2)
    print(feladat_3(7))
    print(feladat_4)
    print(feladat_5(7))
    feladat_6()
    feladat_7()
    print(feladat_8(double_tomb,4))
    print(feladat_9(tomb,5))
    print(feladat_10(tomb,5,2))
    print(feladat_11())
    print(feladat_12(matrix12,3,2))
    print(feladat_13(matrix13, 3, 2))
    print(feladat_14(matrix14,3))
    print(feladat_15(matrix15,2))
    print(feladat_16(matrix16,3,2,transzponalt16))
if __name__ == '__main__':
    main()