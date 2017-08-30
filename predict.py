import json
from probablity_calculation import prob_calc
arturo_probs = json.load(open("arturo_probs.json"))
zareef_probs = json.load(open("zareef_probs.json"))
Test_Text = input("Text: ").lower()
Words = Test_Text.split(" ")
zareef_Chance_Authored = 0.0
arturo_Chance_Authored = 0.0

for words in Words:
    try: zareef_Chance_Authored += zareef_probs[words]
    except: pass
    try: arturo_Chance_Authored += arturo_probs[words]
    except: pass

try:
    Normalized_zareef_chance_authored = zareef_Chance_Authored / (zareef_Chance_Authored + arturo_Chance_Authored) * 100
    Normalized_arturo_chance_authored = arturo_Chance_Authored / (arturo_Chance_Authored + zareef_Chance_Authored) * 100
except:  Normalized_arturo_chance_authored  = Normalized_zareef_chance_authored = 50

print("\nZareef - {}% \nArturo - {}%".format(Normalized_zareef_chance_authored, Normalized_arturo_chance_authored))

Training_Text = json.load(open("training_text.json", "r"))
Training_Text[input("Actual Author: ").lower()] += Test_Text + " "
json.dump(Training_Text, open("training_text.json", "w"))
prob_calc()
