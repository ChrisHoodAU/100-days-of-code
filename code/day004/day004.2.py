# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
number_of_people = len(names)
sucker = random.randint(0, number_of_people - 1)
print(f"{names[sucker]} is going to buy the meal today!")