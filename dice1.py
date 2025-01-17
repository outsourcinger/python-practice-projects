from random import randint

results = []

for _ in range(6):
#dice
    t = [1, 2, 3, 4, 5, 6]
#rolls
    roll1 = t[randint(0,5)]
    roll2 = t[randint(0,5)]
    roll3 = t[randint(0,5)]
    roll4 = t[randint(0,5)]
    # print('You rolled a ', roll1, roll2, roll3, roll4)
    # print('You rolled a {}'.format(roll2))
    # print('You rolled a {}'.format(roll3))
    # print('You rolled a {}'.format(roll4))
    numbers = [roll1, roll2, roll3, roll4]
    numbers.remove(min(numbers))
    sum1 = sum(numbers)
    print("You rolled a", roll1, roll2, roll3, roll4, '\b.' " Your ability score is", sum1)
    result = sum1
    results.append(result)

print("Your ability scores are", results)
list1 = results
list1.sort()
ability1 = list1[0]
ability2 = list1[1]
ability3 = list1[2]
ability4 = list1[3]
ability5 = list1[4]
ability6 = list1[5]
print("Here are your sorted scores.")
print(ability1)
print(ability2)
print(ability3)
print(ability4)
print(ability5)
print(ability6)

str1 = input("Which score would you like to assign to your Strength?")
dex1 = input("Which score would you like to assign to your Dexterity?")
con1 = input("Which score would you like to assign to your Constitution?")
int1 = input("Which score would you like to assign to your Intellegence?")
wis1 = input("Which score would you like to assign to your Wisdom?")
cha1 = input("Which score would you like to assign to your Charisma?")
print("Your ability scores are \n", str1, "Strength \n", dex1, "Dexterity \n", con1, "Constitution \n", int1, "Intellegence \n", wis1, "Wisdom \n", cha1, "Charisma")