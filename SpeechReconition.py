import speech_recognition as sr

def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)
        print('trying')
    try:
        speech_to_text = r.recognize_google(audio)
    except:
        speech_to_text = speech_recognition()
    print('inside function test:',speech_to_text)
    return speech_to_text
