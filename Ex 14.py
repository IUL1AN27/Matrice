n=int(input('Introduceti numarul de linii a matricei:'))
M=[[int(input()) for i in range(n)] for j in range(n)]
print('Matricea este:')
for i in range(len(M)):
    print(M[i])
s1=0
for i in range(0,len(M)):
    s1+=M[i][i]  
s2=0
for i in range(0,len(M)):
    s2+=M[len(M)-i-1][i]
print('Suma diagonalei principale este:', s1) 
print('Suma diagonalei secundare este:',s2)   
s3=0
for i in M:
    for j in i:
        if M.index(i)<i.index(j):
            s3+=j
print('Suma componentelor mai sus de diagonala principala este:', s3)
s4=0
for i in M:
    for j in i:
        if M.index(i)>i.index(j):
            s4+=j
print('Suma componentelor mai jos de diagonala principala este:', s4)
s5=0
for i in M:
    for j in i:
        if M.index(i)+i.index(j)<n-1:
            s5+=j
print('Suma componentelor mai sus de diagonala secundara este:', s5)
s6=0
for i in M:
    for j in i:
        if M.index(i)+i.index(j)>n-1:
            s6+=j
print('Suma componentelor mai jos de diagonala secundara este:', s6)