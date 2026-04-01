def create_matrix(N):
    matrix = []
    for i in range (N):
        column = []
        for j in range (N):
            if abs(j-i) == 1:
                column.append(-1)
            elif (i == j):
                column.append(i+2)
            else:
                column.append(0)
        matrix.append(column)
    return matrix

def d_matrix (m):
    matrix = []
    for i in range (N):
        column = []
        for j in range (N):
            if (i == j):
                column.append(1/i+2)
            else:
                column.append(0)
        matrix.append(column)
    return matrix
        
def mult_matrix(m1, m2, N):
    matrix = []
    for i in range (N):
        row = []
        for j in range (N):
            value = 0
            for k in range(N):
                value = value + m1[i][k]*m2[k][j]
            row.append(value)
        matrix.append(row)
    return matrix
            
