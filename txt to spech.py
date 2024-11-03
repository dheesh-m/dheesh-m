import pyttsx3

txt_speech = pyttsx3.init()

ans  = input("txt conversion:")

txt_speech.say(ans)

txt_speech.runAndWait()