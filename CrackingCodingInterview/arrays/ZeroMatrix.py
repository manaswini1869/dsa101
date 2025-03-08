def ZeroMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    list_zeroes_rows = set()
    list_zeroes_columns = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                list_zeroes_rows.add(i)
                list_zeroes_columns.add(j)

    print("Rows to zero:", list_zeroes_rows)
    print("Columns to zero:", list_zeroes_columns)

    for row in list_zeroes_rows:
        for i in range(n):
            matrix[row][i] = 0

    for column in list_zeroes_columns:
        for i in range(m):
            matrix[i][column] = 0

    print("Modified matrix:")
    print(matrix)

matrix = [[0, 1, 3], [4, 5, 6], [7, 0, 8], [9, 10, 0]]
ZeroMatrix(matrix)
matrix1 = [[0,1,2],[3,4,5]]
ZeroMatrix(matrix1)
