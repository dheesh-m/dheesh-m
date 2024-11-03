import pyttsx3


txt_speech = pyttsx3.init()


txt_speech.setProperty('rate', 150)  
txt_speech.setProperty('volume', 1)  

while True:
   
    ans = input("Enter text for conversion to speech (or type 'exit' to quit): ")

    if ans.lower() == 'exit':
        print("Exiting the program.")
        break

 
    txt_speech.say(ans)

    txt_speech.runAndWait()
