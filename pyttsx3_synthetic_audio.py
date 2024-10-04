import pyttsx3
import pandas as pd

engine = pyttsx3.init()

# set to a different voice
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[41].id)

# set a different rate
rate = engine.getProperty('rate') 
# engine.setProperty('rate', 125)

# dataframe with common voice sentences
data = pd.read_csv('train.tsv', sep='\t')
sentences = data['sentence']

# using 100 sentences from common voice
sentences = sentences[3100: 3105]
#sentences = sentences[3000:3100]

# Show the first few sentences in the slice
print(sentences.head())

index = 100
# loop to create each audio file
for i, j in enumerate(sentences):
  if j != '':
    engine.say(j)
    file = 'pyttsx3_files/pyttsx3_synth_' + str(index) + '.mp3'
    engine.save_to_file(j, file)
    index +=1

engine.runAndWait()


# listing the voices available 
'''
index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1
engine.runAndWait()
'''