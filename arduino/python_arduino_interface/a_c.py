import serial

#have a variable object set as the setup function for proper implementaion, ex. serport=setup('/dev/ttyACM0')
def setup(portnum):
  s=serial.Serial(portnum)
  s.baudrate=9600
  s.port=portnum
  s.open()
  return s

def punch_1(ser,arm):
  if arm=='left':
    ser.write('b')
  if arm=='right':
    ser.write('a')
  
def punch_2(ser,arm):
  if arm=='left':
    ser.write('d')
  if arm=='right':
    ser.write('c')
