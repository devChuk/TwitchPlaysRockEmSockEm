import serial

#have a variable object set as the setup function for proper implementaion, ex. serport=setup('/dev/ttyACM0')
def setup():
  s=serial.Serial(portnum)
  s.baudrate=9600
  s.port=portnum
  s.open()
  return s

def punch_1(ser,arm):
  if arm=='left':
    ser.write(1)
  if arm=='right':
    ser.write(2)
  
def punch_2(ser,arm):
  if arm=='left':
    ser.write(3)
  if arm=='right':
    ser.write(4)
