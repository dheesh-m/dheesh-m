import pyttsx3 

def onStart(): 
 print('starting') 

def onWord(name, location, length): 
 print('word', name, location, length) 

def onEnd(name, completed): 
 print('finishing', name, completed) 

txt_speech = pyttsx3.init() 

txt_speech.connect('started-utterance', onStart) 
txt_speech.connect('started-word', onWord) 
txt_speech.connect('finished-utterance', onEnd) 

sen = 'hello its the robot what can i do for you'


txt_speech.say(sen) 
txt_speech.runAndWait() 
