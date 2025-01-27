import re
from const import numbers

def clear_text(text:str):
    """
    Remove punctuation marks and convert all letters to lowercase.
    """
    text = text.replace("-"," ")
    
    return text.lower()

def split_text(text:str):
    """
    Split a text into words.

    Entry:
    text (str): The text to be split.
    
    Returns:
    list (list): The list of words.
    """
    return re.split(r'\s+', text)

def convert_int(list:list):
    """
    Convert string numbers in a text into integer numbers.

    Entry:
    list (list): The list of strings to be converted.
    """
    for i in range(0,len(list)):
        if list[i] not in numbers:
            raise ValueError (f"Invalid number: {list[i]}")
        list[i] = numbers[list[i]]
    
    return list

def clear_list(list:list):
    """
    Remove None values from the list.

    Entry:
    list (list): The list to be cleaned.
    
    Returns:
    list (list): The cleaned list.
    """
    return [word for word in list if word!=None]

def parse_number(words:list):
    """
    Parse the number words into an integer.
    
    Entry:
    words (list): The list of words to be parsed.
    
    Returns:
    int (int): The parsed number.
    """
    if len(words) > 1:
        _ = [words[0]]
        if words[0] != None:
            if words[0] > 1000:
                words = [words[0]] + [parse_number(words[1:])]
            if words[1] in [100, 10**3, 10**6, 10**9, 10**12, 10**15]:
                words[1] *= words[0]
                words[0] = None

            else:
                words[1] += words[0]
                words[0] = None
                    
        
        words = clear_list(words)
        words = [parse_number(words)]
                    
    return words[0]


# Exemple d'utilisation
while True:
    text = input("Enter a number in letters : ")
    words = clear_text(text)
    if text != "q":
        words = split_text(text)
        words = convert_int(words)
        words = parse_number(words)
        print("result : ", words)
    else:
        break
