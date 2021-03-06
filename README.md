# **돌리와 도트**

#### 부산 학생주도형 제 4회 메이커랑 놀자



# 1. 참가 학생

최재민: 프로그래밍

송찬혁: 3D모델링




# 2. 사용한 재료

방수 스프레이, 소켓 점퍼 MM, MF, FF, 외경 7mm 스프레이 노즐, 내경 7mm 실리콘 튜브, 워터펌프 모터, 아두이노 우노용 USB A to B 케이블, 브레드 보드, Arduino Uno R3 SMD 호환보드, 마이크, 노트북, 에탄올 1L, 소독제 담을 넓고 높은 용기



# 3. 작품 제작 동기

사회에 문제가 되는 많은 것들 중 하나는 욕설이다. 

어떻게 하면 재미있게 욕설을 사용하지 않도록 홍보하면 좋을지 생각하다, 평소에 관심이 있는 AI/딥러닝 및 3D프린터를 활용하여 실체가 보이는 것으로 만들자는 생각이 들어 만들게 되었다.



# 4. 작품 설명

기계의 마이크에 욕설을 하면 입에서 침을 뱉고, 착한 말을 하면 눈에서 감동의 눈물을 흘린다.



## ① 프로그래밍 및 소스코드

### 음성인식 및 통신

 음성인식은 Python의 Speech_recognition 모듈을 사용하였다.
 음성 입력을 받아, 착한 말인지 나쁜 말인지 구분하여 Serial로 아두이노와 통신한다.
 착한 말과 나쁜 말은 머신러닝을 통하여 학습시켰다.
 음성인식 및 통신 코드는 [여기](https://chicken-moo.com/.old/maker/pythonCode)에서 확인할 수 있다.



### 아두이노 모터 제어

아두이노에 관련된 모든 제어는 Serial 모니터를 사용하여 제어할 수 있게 프로그래밍하여, 다른 프로그래밍 언어(Python 등)에서 사용할 수 있게 하였다.
아두이노 모터 제어 코드는 [여기](https://chicken-moo.com/.old/maker/arduinoCode)에서 확인할 수 있다.



### 시리얼 모니터 명령어 도움말

pump : 펌프에 관한 명령을 합니다.

pin : 핀 설정에 관한 명령을 합니다.



#### pump 도움말

pump on 핀번호 : 핀번호의 핀에 입력된 펌프를 작동시킵니다.

pump off 핀번호 : 핀번호의 핀에 입력된 펌프를 작동 중지시킵니다.

pump tick 핀번호 : 핀번호의 핀에 입력된 펌프를 time(기본 1000ms)만큼 작동합니다.

pump time 시간(ms) : tick에서 실행할 시간을 설정합니다. (기본 1000ms)



#### pin 도움말

pin input 핀번호 : 핀번호의 핀을 INPUT으로 설정합니다.

pin output 핀번호 : 핀번호의 핀을 OUTPUT으로 설정합니다.



## ② 모델링 및 프린트

모델링 프로그램으로 블렌더(Blender)를 사용하였다.
 모델의 안쪽에 구멍을 뚫어 아두이노 회로판과 모터가 들어갈 수 있게 디자인하였고,
 눈과 입에 구멍을 뚫어 알코올 소독제가 나올 수 있게 하였다.

모델링 파일은 [여기](https://chicken-moo.com/.old/maker/blender)에서 확인할 수 있다.
