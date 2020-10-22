from gtts import gTTS
import os

mytext = input("enter what you want to speak : ")
language = 'en'

output = gTTS(text=mytext, lang=language, slow=False)

output.save('pyspeech.mp3')
os.system('start pyspeech.mp3')