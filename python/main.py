import serial
import speech_recognition as sr


# pip install pyserial
# pip install SpeechRecognition
# pip install pyaudio
# pip install gTTS
# pip install
# pyaudio wheel file
# https://www.lfd.uci.edu/~gohlke/pythonlibs/


ser = serial.Serial('COM4', 9600)
good = ['안녕', '잘가', '고마워']
bad = ['싫어', '흥']

while True:
    if ser.readable():
        said = " "
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                said = r.recognize_google(audio, language="ko")
                print(said)

            except Exception as e:
                print("음성 인식 실패... : " + str(e))

        txt = said

        for i in good:
            if i in txt:
                print('good word')
                inp = "p tick 9"
                ser.write(inp.encode('utf-8'))
                print(inp)

        for i in bad:
            if i in txt:
                print('bad word')
                inp = "p tick 8"
                ser.write(inp.encode('utf-8'))
                print(inp)


