import serial
# 시리얼 통신 설정
serial1 = serial.Serial("COM12",9600,timeout=1) # 마이크로비트의 포트 번호와 보드 통신 속도를 통해 포트를 열기

# 무한반복
while True:
    microbitData = str(serial1.readline().decode('utf-8')) # 시리얼에서 한줄을 읽고 utf-8로 디코딩을 진행 (디코딩을 하지 않으면 b''와 같은 형식으로 출력됨)
    if microbitData != "": # microbitData 변수에 문자가 있는지 확인
        print(microbitData) # 받은 문자열을 출력

serial1.close()
