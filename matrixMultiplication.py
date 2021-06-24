#matrix multiplication 3 X 3
def acceptMatrix():
    matrix=[]
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(int(input("Enter [ {} ] [ {} ] : ".format(i,j))))
    return matrix

def matrixMultiplication(m1,m2):
     matrix=[]
     for i in range(3):
         matrix.append([])
         for j in range(3):
             row_addition=0
             for k in range(3):
                 row_addition += m1[i][k] * m2[k][j]
             matrix[i].append(row_addition)
     return matrix
    
def displayMatrix(m):
    for i in range(3):
        print("{}".format(m[i]))



while(1):
    
    print("Enter Matrix M1 :")
    m1=acceptMatrix()
    print("Matrix M1 :")
    displayMatrix(m1)

    print("Enter Matrix M2 :")
    m2=acceptMatrix()
    print("Matrix M2 :")
    displayMatrix(m2)

    m3 = matrixMultiplication(m1,m2)
    print("M1 X M2")
    displayMatrix(m3)

    option=input("Enter '1' to exit or press 'Enter' to continue : ")
    if option=="1":
        break