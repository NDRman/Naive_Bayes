import json
def prob_calc():
    Training_Text = json.load(open("training_text.json", "r"))
    print("Calculating probablities for Zareef... \n")
    Zareef_Words = Training_Text["zareef"].split(" ")
    Zareef_Probabilities = {}
    for word in list(set(Zareef_Words)):
        Zareef_Probabilities[word] = Zareef_Words.count(word)/len(Zareef_Words) * 100
    json.dump(Zareef_Probabilities, open("zareef_probs.json", "w"))
    print("Done \n")

    print("Calculating probablities for Arturo... \n")
    Arturo_Words = Training_Text["arturo"].split(" ")
    Arturo_Probabilities = {}
    for word in list(set(Arturo_Words)):
        Arturo_Probabilities[word] = Arturo_Words.count(word)/len(Arturo_Words) * 100
    json.dump(Arturo_Probabilities, open("arturo_probs.json", "w"))
    print("Done \n")
