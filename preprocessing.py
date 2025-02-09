import sys
sys.dont_write_bytecode = True

import re
import numpy as np
import os

# Number of stories used.
TOTAL_NUM_STORIES = len(os.listdir("./dataset"))
NUM_STORIES = 10
# Window size
WINDOW_SIZE = 5


def create_sublists(input_list, window_size):
    """
    Shifting a window through a list
    Window's size is determined by the window_size variable 
    
    For example, if window size is 2:
    ["I","like","hiking","and","biking"]
    
    OUTPUT1[0] -> ['I', 'like', 'hiking']
    OUTPUT1[1] -> ['like', 'hiking', 'and']
    OUTPUT2[0] -> and
    OUTPUT2[1] -> biking
    
    """
    output1 = [input_list[i:i+window_size] for i in range(len(input_list)-window_size+1)]
    output2 = input_list[window_size:]

    # Removing the last combination for output1, because the last combination has no output.
    output1.pop(-1)

    return output1, output2

def predictions_toInt(window:np.array):
    """
    This function converts dtype = "float32" array to dtype="int8" array,
    It gets the highest number and makes it 1, others 0
    As Dense layer is creating outputs in float32 type, this function seemed to be necessary. 
    """
    window = window.tolist()
    maximum = max(window)
    for i,j in enumerate(window):
        if j == maximum:
            window[i] = 1
        else:
            window[i] = 0
    window = np.asarray(window, dtype="int8")
    return window

def remove_spaces(string):
    """
    Removing spaces in the script
    """
    bosluklar = ["   ","    ","     ","      ","       ","        ","         ","          "]
    string = string.replace("\n"," ")
    string = string.replace("\t","")
    
    for i in bosluklar:
        string = string.replace(i," ")
    return string

def load_dictionary(path = "dictionary/dictionary.txt"):
    with open(path,"r",encoding="utf8") as file:
        dictionary_list = [string.replace("\n","") for string in file.readlines()]
        file.close()
        print("Dictionary is loaded successfully.")
    return dictionary_list

if __name__ == "__main__":
    if sys.dont_write_bytecode:
        print("Set __pycache__ disabled.")
    print("Library loaded")
    print("Number of stories used: %d" %(NUM_STORIES))

def numberize_and_save(index:int):
    """
    This function opens one story,
    encodes each words according to their index in dictionary list,
    and saves it in a seperate folder
    """
    os.makedirs("dataset-encrypted", exist_ok=True)
    
    with open(f"dataset/{index}.txt", "r", encoding="utf-8") as file:
        content = remove_spaces(file.read()).upper()
        words = re.findall(regex, content)
    
    # Tüm kelimeleri dictionary'deki indexlere çevir
    numberized = [str(dictionary_list.index(word)) for word in words if word in dictionary_list]
    
    with open(f"dataset-encrypted/{index}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(numberized))

if __name__ == "__main__":
    # List of the words used. This list will have the words unique to avoid repetition 
    dictionary_list = []
    global_word_set = set()

    # This block gets the words in each script, and adds them to the dictionary_index
    for i in range(NUM_STORIES):
            # Reading scripts for each film
            with open(f"dataset/{i}.txt","r",encoding="utf8") as file:
                string = remove_spaces(file.read())
            string = string.upper()

            # We are looking for words that containing alpha characters only
            regex = r"\b[A-Za-z]+\b" # is alpha
            words = re.findall(regex, string)
            global_word_set.update(words)
            print(f"{i}.txt done.")

    dictionary_list = sorted(global_word_set)

    # Writing the dictionary
    os.makedirs("dictionary", exist_ok=True)

    with open("dictionary/dictionary.txt","w+",encoding="utf8") as file:
        string = "\n".join(dictionary_list)
        file.write(string)
        print("Successfully created the file in dictionary/dictionary.txt")

    for i in range(NUM_STORIES):
        numberize_and_save(i)