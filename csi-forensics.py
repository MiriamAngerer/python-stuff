dna = open("dna.txt").read()

match = {}

# hair color
if dna.find("CCAGCAATCGC"):
    match["hair color"] = "black"

elif dna.find("GCCAGTGCCG"):
    match["hair color"] = "brown"

elif dna.find("TTAGCTATCGC"):
    suspect["hair color"] = "blonde"

# Facial shape
if dna.find("GCCACGG"):
    match["facial shape"] = "square"

elif dna.find("ACCACAA"):
    match["facial shape"]  = "round"

elif dna.find("AGGCCTCA"):
    match["facial shape"]  = "oval"

# Eye color
if dna.find("TTGTGGTGGC"):
    match["eye color"] = "blue"

elif dna.find("GGGAGGTGGC"):
    match["eye color"] = "green"

elif dna.find("AAGTAGTGAC"):
    match["eye color"] = "brown"

# Gender
if dna.find("TGAAGGACCTTC"):
    match["gender"] = "female"

elif dna.find("TGCAGGAACTTC"):
    match["gender"] = "male"

# Further characteristic
if dna.find("AAAACCTCA"):
    match["further characteristic"] = "white"

elif dna.find("CGACTACAG"):
    match["further characteristic"] = "black"

elif dna.find("CGCGGGCCG"):
    match["further characteristic"] = "asian"



Eva = {"hair color" : "blonde", "facial_shape" : "oval", "eye color" : "blue", "gender" : "female", "further characteristic" : "white"}
Larisa = {"hair color" : "brown", "facial_shape" : "oval", "eye color" : "brown", "gender" : "female", "further characteristic" : "white"}
Matej = {"hair color" : "black", "facial_shape" : "oval", "eye color" : "blue", "gender" : "male", " further characteristic" : "white"}
Miha = {"hair color" : "brown", "facial_shape" : "square", "eye color" : "green", "gender" : "male", "further characteristic" : "white"}

if Eva == match:
    print "Eva ate all the ice cream."

elif Larisa == match:
    print "Larisa ate all the ice cream."

elif Matej == match:
    print "Matej ate all the ice cream."

elif Miha == match:
    print "Miha ate all the ice cream."

else:
    print "None of the suspects ate the ice cream. The ice cream thief is still out there. Probably looking for more ice cream right now."
    print "---------------------------------------------------------------------"
    print "We are looking for a person with following characteristics:"
    for i in match:
        characteristics = match.items()
        for k, v in characteristics:
            print k, ":", v
        break
    print "---------------------------------------------------------------------"

