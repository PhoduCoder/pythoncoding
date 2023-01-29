#Matrix in Python

matrix = [[col for col in range(0,15,3)] for row in range(4)]

print (matrix)

matrix[1][3]='A'

print (matrix)

print ("Now Transpose")

transpose_matrix = [[col for col in range(4)]for row in range(0,15,3)]

print (transpose_matrix)
