float wait = 1000;
int pinAvailable[14] = { 0 };
// 핀 사용하는 위치의 pinAvailable 값을 1로 변경
void setup() {
  Serial.begin(9600);
}
void command(String data){
  Serial.println();
  int first = data.indexOf(" ");
  int second = data.indexOf(" ",first+1);
  int strlength = data.length();
  String fir = data.substring(0, first);
  String sec = data.substring(first+1, second);
  String tir = data.substring(second+1, strlength);
  if(fir == "pump" || fir == "p"){
    if(sec == "on"){
      if(pinAvailable[tir.toInt()] != 1){
        Serial.println(">> " + tir + "번 핀이 OUTPUT이 아닙니다.");
        command("pin output " + tir);
      }
      digitalWrite(tir.toInt(), HIGH);
      Serial.println(">> " + tir + "번 펌프를 작동시킵니다.");
      
    }
    else if(sec == "off"){
      if(pinAvailable[tir.toInt()] != 1){
        Serial.println(">> " + tir + "번 핀이 OUTPUT이 아닙니다.");
        command("pin output " + tir);
      }
      digitalWrite(tir.toInt(), LOW);
      Serial.println(">> " + tir + "번 펌프를 작동 중지시킵니다.");
      
    }
    else if(sec == "tick"){
      if(pinAvailable[tir.toInt()] != 1){
        Serial.println(">> " + tir + "번 핀이 OUTPUT이 아닙니다.");
        command("pin output " + tir);
      }
      Serial.println(">> " + tir + "번 펌프를 " + String(wait/1000) + "초 만큼 작동시킵니다.");
      digitalWrite(tir.toInt(), HIGH);
      delay(wait);
      digitalWrite(tir.toInt(), LOW);
      
    }
    else if(sec == "time"){
      wait = tir.toInt();
      Serial.println(">> 분무 시간을 " + String(wait/1000) + "초 만큼 설정합니다.");
    }
    else if(sec == "help" || sec == fir){
      Serial.println("---- pump 도움말 ----");
      Serial.println("pump on 핀번호 : 핀번호의 핀에 입력된 펌프를 작동시킵니다.");
      Serial.println("pump off 핀번호 : 핀번호의 핀에 입력된 펌프를 작동 중지시킵니다.");
      Serial.println("pump tick 핀번호 : 핀번호의 핀에 입력된 펌프를 time(기본 1000ms)만큼 작동합니다.");
      Serial.println("pump time 시간(ms) : tick에서 실행할 시간을 설정합니다. (기본 1000ms)");
    }
    else {
      Serial.println(">> " + sec + "는 pump에 없는 명령어입니다.");
      Serial.println(">> pump help를 입력하여 도움말을 확인하세요.");
    }
  }
  else if(fir == "help"){
    Serial.println("---- 도움말 ----");
    Serial.println("pump : 펌프에 관한 명령을 합니다.");
    Serial.println("pin : 핀 설정에 관한 명령을 합니다.");
  }
  else if(fir == "pin"){
    if(sec == "output"){
      pinMode(tir.toInt(), OUTPUT);
      digitalWrite(tir.toInt(), LOW);
      pinAvailable[tir.toInt()] = 1;
      Serial.println(">> " + tir + "번 핀을 OUTPUT으로 설정합니다.");
    }
    else if(sec == "input"){
      pinMode(tir.toInt(), INPUT);
      digitalWrite(tir.toInt(), LOW);
      pinAvailable[tir.toInt()] = 2;
      Serial.println(">> " + tir + "번 핀을 INPUT으로 설정합니다.");
    }
    else if(sec == "help" || sec == fir){
      Serial.println("---- pin 도움말 ----");
      Serial.println("pin input 핀번호 : 핀번호의 핀을 INPUT으로 설정합니다.");
      Serial.println("pin output 핀번호 : 핀번호의 핀을 OUTPUT으로 설정합니다.");
    }
    else{
      Serial.println(">> " + sec + "는 pin에 없는 명령어입니다.");
      Serial.println(">> pin help를 입력하여 도움말을 확인하세요.");
    }
  }
  else{
    Serial.println(">> " + data + "은/는 없는 명령어입니다.");
    Serial.println(">> help를 입력하여 도움말을 확인하세요.");
  }
}
void loop() {
  if(Serial.available()){
    String data = Serial.readStringUntil('\n');
    command(data);
  }
}
