# Short Story Generator

This project utilizes a Keras Sequential model to generate short stories. The model is designed with an LSTM layer followed by a Dense layer to predict the next sequence of words.

## Model Architecture

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ lstm (LSTM)                     │ (None, 64)             │       418,048 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense (Dense)                   │ (None, 1568)           │       101,920 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
```

- **LSTM Layer:** Captures the temporal dependencies in the text data.
- **Dense Layer:** Outputs the probability distribution over the vocabulary of 1568 words extraced from 41 different short stories.
## Dataset

The Dataset is generated by a LLM ChatGPT-4o-mini. 41 different short stories created.
* 21 stories of 10 sentences each,
* 10 stories of 30 sentences each,
* 10 stories of 50 sentences each.

The stories can be found in `./dataset` folder. 

## Project Structure

```
.
├── dictionary
│   └── dictionary.txt
├── main.py
├── model.ipynb
├── model.keras
├── model-usage.py
├── plotter.py
├── preprocessing.py
└── rename.py
```
* **dictionary.txt** is a vocabulary list of known words by the model. The model will only generate using words in this file. The file is generated automatically by `preprocessing.py` and **it should not be edited.**
* **main.py** is the file to use the program. 
* **model.ipynb** is a internactive python notebook file and it is where the model is created and trained. You can take a look at the model creation process, model training process and evaluation of the model. Desired changes in the model can be made in this part.
* **model.keras** is a file that generated automatically by `model.ipynb` and it contains the Sequential keras model. **This file is the model itself and it should not be touched.**
* **model-usage.py** is a python file that the model is run and generate outputs in the background. **It is essential to the main program run, please do not edit.**
* **plotter.py** is helper plotter library to visualize the evaluation of model. It is used by `model.ipynb` in evaluation part.
* **preprocessing.py** is a helper library that holds some variables and functions. The file that is called by `model.ipynb` to generate the dictionary. In case of it running alone, a new dictionary file will be generated by the script.
* **rename.py** is a helper library to rename all the files under `/dataset` folder to name them in correct order. **Don't run.**


## Requirements

- Python 3.x
- TensorFlow >=2.17.0
- Keras >=3.6.0
- NumPy
- matplotlib

**Note: The project might work unexpectedly in older versions.**
## Running on your local environment

1. Clone the repository and switch to the working directory
```
git clone https://github.com/yegekucuk/short-story-generator.git
cd short-story-generator
```
2. If you want to change the settings such as number of generated words or generated files (stories), consider opening `main.py` with your text editor. Let's say nano in this case of Ubuntu. You can edit the variables in the top of the program. The default for story length is 105 (100 generated + 5 initializing) and for generated files it is 2.  
3. Run the file.
```
python3 main.py
```
4. You will find the outputs such as `story_n.txt`.
## Results
As of the results, the model's training accuracy is 98% and test accuracy come out as 16% which means the model is overfitting. It should be taken into consideration that model is classifying among 1568 classes. It is thought the model might be overfitting because of the lack of big data, using wrong model architecture, choosing wrong hyperparameters or wrong preprocessing of the data. Even so, the model can can generate a satisfactory amount of meaningful output before going into an infinite loop. **The recommended way to use the model is generating 100 words for each story to match the length of a story with 10 sentences.**
