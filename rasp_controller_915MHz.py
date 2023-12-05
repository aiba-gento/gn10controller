import serial

serial_port = '/dev/ttyS0'
serial_bound_rate = 9600

# シリアルポートとボートレートを設定します
mySerial = serial.Serial(serial_port, serial_bound_rate)

mySerial.write(b'AT+CFM=1\r\n')

# レスポンスを読み取ります
response = mySerial.readline()
print(response)

# 受信データを読み取ります
received_data = mySerial.readline()
print(received_data)

mySerial.close()