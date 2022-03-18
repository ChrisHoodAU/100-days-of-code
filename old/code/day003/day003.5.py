# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bothnames = (name1.lower() + name2.lower())
print(bothnames)
t = bothnames.count("t")
r = bothnames.count("r")
u = bothnames.count("u")
e = bothnames.count("e")
l = bothnames.count("l")
o = bothnames.count("o")
v = bothnames.count("v")
score = str(t + r + u + e) + str(l + o + v + e)
if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")