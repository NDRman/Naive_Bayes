#Adding Data to the Naive Bayes
import json
from probablity_calculation import prob_calc
Training_Text = json.load(open("training_text.json", "r"))
Training_Text[input("Author: ").lower()] += input("Training Text: ").lower() + " "
json.dump(Training_Text, open("training_text.json", "w"))
print("\n" + "Zareef: " + Training_Text["zareef"])
print("\n" + "Arturo: " + Training_Text["arturo"] + "\n")
prob_calc()
