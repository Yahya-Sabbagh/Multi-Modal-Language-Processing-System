#import library

import speech_recognition as sr
# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone(1) as source:
    print("Talk")
    r.adjust_for_ambient_noise(source)
    audio_text = r.listen(source, timeout=5, phrase_time_limit=5)
    print("Time over, thanks")
# recognize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")