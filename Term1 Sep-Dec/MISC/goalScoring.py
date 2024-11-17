MatchesPlayed = int(input("Enter matches played: "))
OneGoal = int(input("Number of matches with 1 goal: "))
TwoGoal = int(input("Number of matches with 2 goals: "))
MoreThenTwo = int(input("Number of matches with more than 2 goals: "))

print(f"The number of mathes with no score was {MatchesPlayed-OneGoal-TwoGoal-MoreThenTwo}")
print(f"The number of matches with a score more then one is {TwoGoal+MoreThenTwo}")
print(f"The number of matches with less then 3 goals is {OneGoal+TwoGoal}")