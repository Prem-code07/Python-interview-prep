mat = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(mat)
cols = len(mat[0])
transpose = []

for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(mat[j][i])
    transpose.append(new_row)

print(transpose)
