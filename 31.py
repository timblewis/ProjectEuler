ways = [[0 for x in range(9)] for x in range(201)]

c = [0,1,2,5,10,20,50,100,200]

for i in range(1,9):
    for j in range(201):
        ways[j][i] += ways[j][i-1]
        if j == c[i]:
            ways[j][i] += 1
        elif j > c[i]:
            ways[j][i] += ways[j-c[i]][i]

print(str(ways[200][8]))