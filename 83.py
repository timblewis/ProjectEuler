# Problem:
# Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.

# Solution:
# Dijkstra's Algorithm

import io

# Open the file
with io.open('p083_matrix.txt', 'r') as file:
    text = file.read()
# Remove any space at the begining or end of the file.
text = text.strip()
# Extract each row.
rows = text.split('\n')
# Extract each entry of the matrix from each row and convert the string to an integer.
matrix = [[int(x) for x in rows[i].split(',')] for i in range(len(rows))]

# Determine size of Matrix (just for convenience).
numRows = len(matrix)
numCols = len(matrix[0])

# The final shortest paths to each entry of the matrix (initialized to 0 if shortest path has not been found yet).
shortestPathLength = [[0 for i in range(numCols)] for j in range(numRows)]

# List of "unvisited" nodes and the current shortest path to them.
# [row, col, l]
# l is the shortest length path found so far to get to (row, col).
# We start at the upper left corner (0,0)
work = [[0,0,matrix[0][0]]]

# While there are still unvisited nodes.
while(len(work) > 0):

    # Find the unvisited node with the shortest path to it.
    minLIndex = 0
    minLWork = work[0]
    for i in range(1,len(work)):
        if work[i][2] < minLWork[2]:
            minLIndex = i
            minLWork = work[i]

    # Then visit the found node (it is "safe" to set the length of the path to that node).
    work.pop(minLIndex)
    row = minLWork[0]
    col = minLWork[1]
    l = minLWork[2]
    shortestPathLength[row][col] = l

    # If the neighboring nodes' lengths have not already been set then their smallest path needs to be updated.
    needToAddLeft = (row > 0) and (shortestPathLength[row-1][col] == 0)
    needToAddRight = (row < numRows-1) and (shortestPathLength[row+1][col] == 0)
    needToAddAbove = (col > 0) and (shortestPathLength[row][col-1] == 0)
    needToAddBelow = (col < numCols-1) and (shortestPathLength[row][col+1] == 0)

    # Search through all the work to find if a neighboring node is already in the list.
    for w in work:
        # If the work represents a neighboring node
        if abs(w[0] - row) + abs(w[1] - col) == 1:
            # Update the shortest path to that node
            w[2] = min(w[2], l + matrix[w[0]][w[1]])
            # We don't have to add that node to the list of work.
            if w[0] == row - 1:
                needToAddLeft = False
            elif w[0] == row + 1:
                needToAddRight = False
            elif w[1] == col - 1:
                needToAddAbove = False
            else:
                needToAddBelow = False

    # Add the neighbors to the list of work if it is needed.
    if needToAddLeft:
        work.append([row-1, col, l + matrix[row-1][col]])
    if needToAddRight:
        work.append([row+1, col, l + matrix[row+1][col]])
    if needToAddAbove:
        work.append([row, col-1, l + matrix[row][col-1]])
    if needToAddBelow:
        work.append([row, col+1, l + matrix[row][col+1]])

# Print the shortest path to the lower right corner.
print(shortestPathLength[numRows-1][numCols-1])