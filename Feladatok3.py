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

matrix13=np.empty((3,2),np.int)
matrix13[0][0]=1
matrix13[0][1] = 69
matrix13[1][0] = 32
matrix13[1][1] = 9
matrix13[2][0] = 2
matrix13[2][1] = 19
def feladat_13(matrix,n,m):
    t=np.empty(m,int)
    matrix_uj=((n,m),np.int)
    for i in range(m):
        min=matrix[i][0]
        for j in range(n):
            if matrix[j][i]<min:
                min=matrix[j][i]
        for k in range(n):
            matrix_uj[k][i]=matrix[j][i]-min
    for q in range(n):
        for w in range(m):
            print(matrix_uj[q][w], end=" ")
        print()

matrix14=np.empty((3,3),np.int)
matrix14[0][0]=1
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

def main():
    feladat_1()
    print(feladat_2)
    print(feladat_3(7))
    print(feladat_4)
    print(feladat_5(7))
    print(feladat_14(matrix14,3))
    print(feladat_15(matrix15, 2))
if __name__ == '__main__':
    main()