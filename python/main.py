import serial
import speech_recognition as sr


# pip install pyserial
# pip install SpeechRecognition
# pip install pyaudio
# pip install gTTS
# pip install
# pyaudio wheel file
# https://www.lfd.uci.edu/~gohlke/pythonlibs/

print('COM 설정 : ', end='')
com = input()
print('통신 설정 : ', end='')
srt = input()

ser = serial.Serial('COM' + com, srt)

good = []
goodTxt = open("good.txt", 'r')
while True:
    line = goodTxt.readline()
    if not line: break
    good.append(line.strip('\n'))

print("좋은말 데이터 : ", end='')
print(good)

bad = []
badTxt = open("bad.txt", 'r')
while True:
    line = badTxt.readline()
    if not line: break
    bad.append(line.strip('\n'))

print("나쁜말 데이터 : ", end='')
print(bad)

while True:
    if ser.readable():
        print("\n> 음성 인식 시작")
        said = " "
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            print("> 음성 인식 분석 중")
            try:
                said = r.recognize_google(audio, language="ko")
                print("> 음성 인식 성공 : " + said)

            except Exception as e:
                print("> 음성 인식 실패")

        txt = said

        for i in good:
            if i in txt:
                print('> 좋은 말 감지, 9번 펌프 실행')
                inp = "p tick 9"
                ser.write(inp.encode('utf-8'))

        for i in bad:
            if i in txt:
                print('>> 나쁜 말 감지, 8번 펌프 실행')
                inp = "p tick 8"
                ser.write(inp.encode('utf-8'))
