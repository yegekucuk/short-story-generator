import sys
sys.dont_write_bytecode = True

from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.utils import to_categorical # type: ignore
from preprocessing import *
from time import sleep
import random
from main import LENGTH_EACH_STORY, NUMBER_OF_STORIES_TO_GENERATE

# Loading the dictionary
dictionary_list = load_dictionary()

# Randomly selecting first few words of the story
model = load_model("model.keras")
print("Model is imported successfully")

def predict_a_word(inputs):
  """
  This model predicts a word according to the inputs
  Inputs is a list and it contains 5 strings
  """
  # Converting Strings to Categorical
  window = inputs.copy()
  window = [[dictionary_list.index(word)] for word in window]
  categorical = to_categorical(window,num_classes=len(dictionary_list))

  # Predicting
  categorical = np.reshape(categorical,(1, WINDOW_SIZE, len(dictionary_list)))
  pred = model.predict(categorical)
  print(pred.shape)
  pred = np.reshape(pred,len(dictionary_list))
  pred = predictions_toInt(pred)

  # Getting the predicted words, which is only 1 word
  # The code was changed to see multiple outputs during the test
  # But this code works for 1 word also
  ones = []
  for i,j in enumerate(pred.tolist()):
    if j == 1:
      ones.append(i)
  new_words = [dictionary_list[ones[i]] for i in range(len(ones))]
  return new_words[0]

# Generate the story
def generate_story(length=100, num_of_stories=1):
  for story_index in range(num_of_stories):
    story = random.sample(dictionary_list, k=WINDOW_SIZE)
    for i in range(length):
        print(i)
        input = story[-WINDOW_SIZE:]
        new_word = predict_a_word(input)
        story.append(new_word)
        os.system("clear")
        print(" ".join(story))
        #sleep(0.1)
    os.system("clear")
    story_string = " ".join(story).capitalize() + "."
    print(story_string)
    with open(f"story_{story_index}.txt","w") as file:
      file.write(story_string)
    

generate_story(LENGTH_EACH_STORY, NUMBER_OF_STORIES_TO_GENERATE)