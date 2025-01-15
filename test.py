import re
from const import *

def parse_unit(string):
    mots = re.split(r'(thousand|million)', string)

    # Recomposer la chaîne en ajoutant les mots divisés
    resultat = []
    temp_str = ""
    for mot in mots:
        if mot in {"hundred", "thousand", "million"}:
            temp_str += " " + mot
            resultat.append(temp_str.strip())
            temp_str = ""
        else:
            temp_str += " " + mot.strip()
    
    return resultat

def convert_a_unit(string):
    ls = string.split(" ")
    unit = numbers[ls.pop()]
    result = 0

    for elt in ls:
        nb = numbers[elt]
        

def converter(string):
    result = parse_unit(chaine.lower())
    for elt in result:
        e = convert_a_unit(elt)
    
    return result


# Votre chaîne
chaine = "five hundred thousand thirty million four hundred fifty six thousand seven hundred twenty nine"

result = converter(chaine)

# Résultat final
print(result)

