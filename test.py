import re
from const import numbers

def convert_int(list):
    for i in range(0,len(list)):
        if list[i] not in numbers:
            continue
        list[i] = numbers[list[i]]

def parse_number(words):
    if len(words) > 1:
        if words[0] != None:

            # combine tens
            if 20 <= words[0] <= 90:
                if 0 < words[1] < 10:
                    words[1] += words[0]
                    del words[0]
            
            # combine hundreds
            elif words[1] == 100:
                if 0 < words[0] < 10:
                    words[1] *= words[0]
                    del words[0]
            
            else:
                words = [words[0]] + parse_number(words[1:])
                    
    return words


# Exemple d'utilisation
text = "five hundred forty eight thousand thirty million four hundred fifty six thousand seven hundred twenty nine"
words = re.split(r'\s+', text)
convert_int(words)
words = parse_number(words)
print(words)
