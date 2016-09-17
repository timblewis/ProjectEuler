# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#
# Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
#
# What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

# PeterScoreProb[i] contains the probability the sum of Peter's rolls is i
PeterScoreProb = [0]*37
ColinScoreProb = [0]*37

# Compute the probability of getting scores for rolling i die by first computing the probability of getting scores for rolling i-1 die
# With 0 die the probability Peter rolls a total of 0 is 1
PeterScoreProb[0] = 1
# Start computing probabilities for rolling 1 die and work up to 9
for dice in range(1,10):
    # Start updating scores working from top to bottom so we don't overwrite a score we need in the future
    for score in range(4*dice,-1,-1):
        # The probability for rolling a sum of k with i dice is 1/4 * the sum of the probability of rolling k-1, k-2, k-3, and k-4 with i-1 dice
        PeterScoreProb[score] = 0
        for previous in range(max(0, score - 4), score):
            PeterScoreProb[score] += PeterScoreProb[previous]/4


ColinScoreProb[0] = 1
for dice in range(1,7):
    for score in range(6*dice,-1,-1):
        ColinScoreProb[score] = 0
        for previous in range(max(0, score - 6), score):
            ColinScoreProb[score] += ColinScoreProb[previous]/6

# PeterTailSum[i] is the probability that Peter has a score higher than i
PeterTailSum = [0]*37
# the probability peter rolls greater than i = the probability peter rolls i+1 + the probability peter rolls greater than i+1
for score in range(35, -1,-1):
    PeterTailSum[score] = PeterTailSum[score+1] + PeterScoreProb[score+1]

# Peter's win probability is the sum of the probability Colin rolls a score times the probability Peter rolls greater than that score
PeterWinProb = 0
for score in range(0,37):
    PeterWinProb += ColinScoreProb[score]*PeterTailSum[score]

# Print result
print(PeterWinProb)