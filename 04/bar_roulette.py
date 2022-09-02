import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") # Will dividie into a list
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
no_of_elements = int(len(names))
random_number = random.randint(0,no_of_elements-1)
person = names[random_number]

print(f"{person} is going to buy the meal today!")
