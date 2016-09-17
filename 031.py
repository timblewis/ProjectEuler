# Problem:
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

# Solution:
# Dynamic programming

# Array that contains the number of ways to make a certain amount of money using a certain number of the types of coins
# Example: ways[x][y] = the number of ways to make x cents using only the first y coins
# Note: We could save memory by only keeping track of the number of ways for the previous coin
ways = [[0 for x in range(9)] for x in range(201)]

# The number of cents each coin is worth
c = [0,1,2,5,10,20,50,100,200]

# For each of the 8 coins
# Note: for any value there are 0 ways to make that value using 0 coins so this value is skipped
for i in range(1,9):
    # For all the different possible values we could want to make
    for j in range(201):
        # Add the number of ways to make that value without using coin i
        ways[j][i] = ways[j][i-1]
        # If the value we are trying to make is exactly the same as the coin we can use a single coin to make the value
        if j == c[i]:
            ways[j][i] += 1
        # If the value we are trying to make is larger than the coins value then
        # the total number of ways of making the value using the coin at least once is ways[j-c[i]][i]
        elif j > c[i]:
            ways[j][i] += ways[j-c[i]][i]

# Print the number of ways to make 200 cents using all 8 coins
print(str(ways[200][8]))