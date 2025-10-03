def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0] * rows  for _ in range(cols )]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix