import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
