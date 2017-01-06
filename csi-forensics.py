dna = open("dna.txt").read()

Eva = {"hair color" : "blonde", "facial shape" : "oval", "eye color" : "blue", "gender" : "female", "further characteristic" : "white"}
Larisa = {"hair color" : "brown", "facial shape" : "oval", "eye color" : "brown", "gender" : "female", "further characteristic" : "white"}
Matej = {"hair color" : "black", "facial shape" : "oval", "eye color" : "blue", "gender" : "male", " further characteristic" : "white"}
Miha = {"hair color" : "brown", "facial shape" : "square", "eye color" : "green", "gender" : "male", "further characteristic" : "white"}

match = {}

# hair color
if "CCAGCAATCGC" in dna:
    match["hair color"] = "black"

elif "GCCAGTGCCG" in dna:
    match["hair color"] = "brown"

elif "TTAGCTATCGC" in dna:
    match["hair color"] = "blonde"

# Facial shape
if "GCCACGG" in dna:
    match["facial shape"] = "square"

elif "ACCACAA" in dna:
    match["facial shape"]  = "round"

elif "AGGCCTCA" in dna:
    match["facial shape"]  = "oval"

# Eye color
if "TTGTGGTGGC" in dna:
    match["eye color"] = "blue"

elif "GGGAGGTGGC" in dna:
    match["eye color"] = "green"

elif "AAGTAGTGAC" in dna:
    match["eye color"] = "brown"

# Gender
if "TGAAGGACCTTC" in dna:
    match["gender"] = "female"

elif "TGCAGGAACTTC" in dna:
    match["gender"] = "male"

# Further characteristic
if "AAAACCTCA" in dna:
    match["further characteristic"] = "white"

elif "CGACTACAG" in dna:
    match["further characteristic"] = "black"

elif "CGCGGGCCG" in dna:
    match["further characteristic"] = "asian"
        

        
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
 

