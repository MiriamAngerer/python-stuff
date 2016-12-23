dna = open("dna.txt").read()

suspect = {}

# hair color
if dna.find('CCAGCAATCGC'):
    suspect["hair_color"] = "black"

elif dna.find('GCCAGTGCCG'):
    suspect["hair_color"] = "brown"

elif dna.find('TTAGCTATCGC'):
    suspect["hair_color"] = "blonde"

# Facial shape
if dna.find('GCCACGG'):
    suspect["facial_shape"] = "square"

elif dna.find('ACCACAA'):
    suspect["facial_shape"]  = "round"

elif dna.find('AGGCCTCA'):
    suspect["facial_shape"]  = "oval"

# Eye color
if dna.find('TTGTGGTGGC'):
    suspect["eye_color"] = "blue"

elif dna.find('GGGAGGTGGC'):
    suspect["eye_color"] = "green"

elif dna.find('AAGTAGTGAC'):
    suspect["eye_color"] = "brown"

# Gender
if dna.find('TGAAGGACCTTC'):
    suspect["gender"] = "female"

elif dna.find('TGCAGGAACTTC'):
    suspect["gender"] = "male"

# Skin Color
if dna.find('TGAAGGACCTTC'):
    suspect["skin_color"] = "white"

elif dna.find('CGACTACAG'):
    suspect["skin_color"] = "black"

Eva = {"hair_color" : "blonde", "facial_shape" : "oval", "eye_color" : "blue", "gender" : "female", "skin_color" : "white"}
Larisa = {"hair_color" : "brown", "facial_shape" : "oval", "eye_color" : "brown", "gender" : "female", "skin_color" : "white"}
Matej = {"hair_color" : "black", "facial_shape" : "oval", "eye_color" : "blue", "gender" : "male", "skin_color" : "white"}
Miha = {"hair_color" : "brown", "facial_shape" : "square", "eye_color" : "green", "gender" : "male", "skin_color" : "white"}

if Eva == suspect:
    print "Eva ate all the ice cream."

elif Larisa == suspect:
    print "Larisa ate all the ice cream."

elif Matej == suspect:
    print "Matej ate all the ice cream."

elif Miha == suspect:
    print "Miha ate all the ice cream."

else:
    print "None of the suspects ate the ice cream. The ice cream thief is still out there. Probably eating ice cream."


