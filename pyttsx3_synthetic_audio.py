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

# using 500 sentences from common voice
sentences = sentences[60000: 60500]

# Show the first few sentences in the slice
print(sentences.head())

# loop to create each audio file
for i, j in enumerate(sentences):
  if j != '':
    engine.say(j)
    file = 'pyttsx3_files/pyttsx3_synth_' + str(i) + '.mp3'
    engine.save_to_file(j, file)
    # index +=1

engine.runAndWait()


# listing the voices available 
'''
index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1
engine.runAndWait()
'''

'''
# looping through 7 of the voices
voices = engine.getProperty('voices')
voice_indexes = [0, 7, 10, 17, 28, 33, 37]

for index in voice_indexes:
   print(f'index-> {index} -- {voices[index].name}')
   
   engine.setProperty('voice', voices[index].id)
   engine.say("Hello, this is voice number" + str(index)+ " " + voices[index].name +  " I am not a robot.")
   index +=1

engine.runAndWait()
'''

# looping through all voices
'''
index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   
   engine.setProperty('voice', voices[index].id)
   engine.say("Hello, this is voice number" + str(index)+ " " + voice.name +  " I am not a robot.")
   index +=1

engine.runAndWait()

'''