import speech_recognition as sr

def capture_voice():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak your answer")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except:
        return "Speech not recognized"