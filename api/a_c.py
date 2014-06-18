import serial

#have a variable object set as the setup function for proper implementaion, ex. serport=setup('/dev/ttyACM0')
def setup(portnum):
  s=serial.Serial(portnum)
  s.baudrate=9600
  s.port=portnum
  s.open()
  return s

def punch(ser,punch_letter):
  ser.write(punch_letter)
