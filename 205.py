# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#
# Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
#
# What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

# Returns an array with the probabilities of rolling totals given dice number of dice with faces number of faces
# Compute the probability of getting scores for rolling i die by first computing the probability of getting scores for rolling i-1 die
def RollSumProbabilities(dice,faces):
    # rollSumProbabilities[k] is the probability that a roll gives a sum of k
    rollSumProbabilities = [0]*(dice*faces + 1)
    # With 0 die the probability Peter rolls a total of 0 is 1
    rollSumProbabilities[0] = 1
    # Start computing probabilities for rolling 1 die and work up to dice
    for d in range(dice):
        # Start updating scores working from top to bottom so we don't overwrite a score we need in the future
        for score in range(faces*(d+1),-1,-1):
            # The probability for rolling a sum of k with i dice is 1/faces * the sum of the probability of rolling k-1, k-2, ..., k-faces with i-1 dice
            rollSumProbabilities[score] = sum(rollSumProbabilities[max(0, score-faces):score])/faces
    # Return the result
    return rollSumProbabilities

# Peter rolls 9 dice with 4 sides
PeterScoreProb = RollSumProbabilities(9,4)
# Colin rolls 6 dice with 6 sides
ColinScoreProb = RollSumProbabilities(6,6)


# PeterTailSum[i] is the probability that Peter has a score higher than i
PeterTailSum = [0]*37
# the probability peter rolls greater than i = the probability peter rolls i+1 + the probability peter rolls greater than i+1
for score in range(35, -1,-1):
    PeterTailSum[score] = PeterTailSum[score+1] + PeterScoreProb[score+1]

# Peter's win probability is the sum of the probability Colin rolls a score times the probability Peter rolls greater than that score
PeterWinProb = sum([ColinScoreProb[i]*PeterTailSum[i] for i in range(37)])

# Print result
print(PeterWinProb)