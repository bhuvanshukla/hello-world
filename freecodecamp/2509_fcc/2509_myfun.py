def rotate(matrix):
	"""
	Rotate the matrix 90 degrees clockwise
	"""
    m, n = len(matrix), len(matrix[0])
    # Create a new matrix with swapped dimensions
    rotated = [[0] * m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            rotated[j][m - 1 - i] = matrix[i][j]
    
    return rotated

def is_mirror(str1, str2):
	"""
	A string is considered a mirror if it contains the same letters in reverse order.
	Treat uppercase and lowercase letters as distinct.
	Ignore all non-alphabetical characters.
	"""
    str1cleaned = ''.join(filter(str.isalpha,str1))
    str2cleaned = ''.join(filter(str.isalpha,str2))
    return str1cleaned == str2cleaned[::-1]

