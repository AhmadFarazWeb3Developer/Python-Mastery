import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

# Initialize the pyttsx3 engine
engine = pyttsx3.init()


def speakText(command):
    try:
        with sr.Microphone() as source:
            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Say something...")
            audio = r.listen(source)
            myText = r.recognize_google(audio)
            myText = myText.lower()
            print("You said: " + myText)
            return myText
    except sr.RequestError as e:
        print("Couldn't request results; {0}".format(e))
    except sr.UnknownValueError:
        print('Unknown error occurred')
    return ""


def outputText(text):
    # Write text to file
    with open('./myFile.txt', 'a') as f:
        f.write(text)
        f.write('\n')

    print('Wrote text to file')


def speakOutput(text):
    # Speak the output using pyttsx3
    engine.say(text)
    engine.runAndWait()


# Example of how to use both functions
if __name__ == "__main__":
    command = speakText("Please speak something")
    if command:
        outputText(command)
        speakOutput(f"You said: {command}")
