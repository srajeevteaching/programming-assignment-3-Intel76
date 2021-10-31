# Programmers: Hanna Magan
# Course: CS151-02, Dr.Rajeev
# Date: 10/28/21
# Pa Assignment:  3
# Problem Statement: "calculate various sports statistics for the user, based on the user’s choice
# Input:  football, quidditch gymnastics

print("Please enter a valid sport type: football, quidditch, or gymnast.")
choice = input("Please enter which sport you would like to choose:")

football= input("football")
quidditch= input("quidditch")
gymnast = input("gymnast")

football
interception = input("Please enter your number of interceptions made.")
completion = input("Please enter your number of completions made.")
attempt = input("Please enter your number of attempts made.")
passing_yard = input("Please enter your number of passing yards made.")
touchdown_passess = input("Please enter your number of touchdown passes made.")
football_score = 100 * ((5 * (completion / attempt - 0.3)) + (0.25 * (passing_yard / attempt - 3)) + (20 * (touchdown_passess/attempt)) + 2.375 - (25 * interception / attempt))/ 6
print(football_score)

# quidditch function
quidditch
goals = input("Please enter your number of scores made.")
print(goals)
quidditch_score = input("quidditch_score")
quidditch_score = float(10 * goals)
snitch = input("Did you catch the golden snitch? yes or no?")
if snitch == "yes":
    quidditch_score += 30
elif snitch == "no":
    quidditch_score += 0
print(quidditch_score)

if input("gymnast"):
   difficulty = input("Please enter the difficulty score:")
   score1 = input("Please enter the first score:")
   score2 = input("Please enter the second score:")
   score3 = input("Please enter the third score:")
   score4 = input("Please enter the fourth score:")
   score5 = input("Please enter the fifth score:")
   gymnast_rating = gymnast (score1, score2, score3, score4, score5, difficulty)
   print("The rating of your gymnast is:", gymnast_rating)