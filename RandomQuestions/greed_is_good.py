# Greed is a dice game played with five six-sided dice.
# Your mission, should you choose to accept it, is to score a throw according to these rules.
# You will always be given an array with five six-sided dice values.

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point

#  A single die can only be counted once in each roll. For example,
#  a given "5" can only count as part of a triplet (contributing to the 500 points)
#  or as a single 50 points, but not both in the same roll.

#  Example scoring

#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

#  In some languages, it is possible to mutate the input to the function.
#  This is something that you should never do. If you mutate the input,
#  you will not be able to pass all the tests.

# Input is an array of 5 numbers which can be 1-6.

# My solution.
def score(dice):
    totalScore = 0
    diceDictionary = {e: dice.count(e) for e in set(dice)}

    for key, value in diceDictionary.items():
        if 3 == value:
            if key == 1:
                totalScore += 1000
            elif key == 2:
                totalScore += 200
            elif key == 3:
                totalScore += 300
            elif key == 4:
                totalScore += 400
            elif key == 5:
                totalScore += 500
            elif key == 6:
                totalScore += 600
        if value <= 2:
            if key == 1:
                totalScore += value * 100
            elif key == 5:
                totalScore += value * 50
        if 4 == value:
            if key == 1:
                totalScore += 1000
                totalScore += 100
            elif key == 2:
                totalScore += 200
            elif key == 3:
                totalScore += 300
            elif key == 4:
                totalScore += 400
            elif key == 5:
                totalScore += 500
                totalScore += 50
            elif key == 6:
                totalScore += 600
        if 5 == value:
            if key == 1:
                totalScore += 1000
                totalScore += 2 * 100
            elif key == 2:
                totalScore += 200
            elif key == 3:
                totalScore += 300
            elif key == 4:
                totalScore += 400
            elif key == 5:
                totalScore += 500
                totalScore += 2 * 50
            elif key == 6:
                totalScore += 600

    return totalScore


# print(score([2, 3, 4, 6, 2]))           # 0
# print(score([4, 4, 4, 3, 3]))           # 400
# print(score([2, 4, 4, 5, 4]))           # 450
# print(score([5, 1, 3, 4, 1]))           # 250
# print(score([1, 1, 1, 3, 1]))           # 1100
# print(score([3, 3, 3, 3, 3]))           # 300

# Someone else's clever answer.
def score2(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1

  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum 

print(score2([2, 3, 4, 6, 2]))           # 0
print(score2([4, 4, 4, 3, 3]))           # 400
print(score2([2, 4, 4, 5, 4]))           # 450
print(score2([5, 1, 3, 4, 1]))           # 250
print(score2([1, 1, 1, 3, 1]))           # 1100
print(score2([3, 3, 3, 3, 3]))           # 300