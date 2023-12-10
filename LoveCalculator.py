print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")

names_together = name1 + name2
low_names = names_together.lower()

name_count_true = low_names.count("t") + low_names.count("r") + low_names.count("u") + low_names.count("e")
name_count_love = low_names.count("l") + low_names.count("o") + low_names.count("v") + low_names.count("e")
combined_names = str(name_count_true) + str(name_count_love) 

if 10 >= int(combined_names) or int(combined_names) <= 90:
  print (f"Your score is {combined_names}, you go together like coke and mentos.")
elif 40 <= int(combined_names) <= 50:
  print(f"Your score is {combined_names}, you are alright together.")
else:
    print(f"Your score is {combined_names}.")
