import serial
import speech_recognition as sr
import os

# pip install pyserial
# pip install SpeechRecognition
# pip install gTTS
# pyaudio wheel file
# pip install 휠파일
# https://www.lfd.uci.edu/~gohlke/pythonlibs/

os.system('title 돌리와 도트가 젤 좋아')
os.system('color 03')
os.system('mode con cols=50 lines=10')
os.system('cls')

print('\n > COM 설정 : ', end='')
com = input()
print(' > 통신 설정 : ', end='')
srt = input()

ser = serial.Serial('COM' + com, srt)

good = []
goodTxt = open("good.txt", 'r')
while True:
    line = goodTxt.readline()
    if not line: break
    good.append(line.strip('\n'))


bad = []
badTxt = open("bad.txt", 'r')
while True:
    line = badTxt.readline()
    if not line: break
    bad.append(line.strip('\n'))


while True:
    if ser.readable():
        os.system('cls')
        # print("좋은말 데이터 : ", end='')
        # print(good)
        # print("나쁜말 데이터 : ", end='')
        # print(bad)
        print("\n > 언어 데이터 리로드")
        good = []
        goodTxt = open("good.txt", 'r')
        while True:
            line = goodTxt.readline()
            if not line: break
            good.append(line.strip('\n'))

        bad = []
        badTxt = open("bad.txt", 'r')
        while True:
            line = badTxt.readline()
            if not line: break
            bad.append(line.strip('\n'))

        print(" > 음성 인식 시작")
        said = " "
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            print(" > 음성 인식 분석 중")
            try:
                said = r.recognize_google(audio, language="ko")
                print(" > 음성 인식 성공 : " + said)

            except Exception as e:
                print(" > 음성 인식 실패")

        txt = said
        badW = 0

        for i in bad:
            if i in txt:
                print(' > 나쁜 말 감지, 8번 펌프 실행')
                inp = "p tick 8"
                ser.write(inp.encode('utf-8'))
                badW = 1

        if badW == 0:
            for i in good:
                if i in txt:
                    print(' > 좋은 말 감지, 9번 펌프 실행')
                    inp = "p tick 9"
                    ser.write(inp.encode('utf-8'))

    print('\n ', end='')
    os.system('pause')
