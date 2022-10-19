from djitellopy import Tello
import time

import serial
ser = serial.Serial("COM4", 9600)

t = Tello()
t.connect()
print(t.get_battery())
t.takeoff()
# t.move_up(30)
print("Configuration executed successfully")
time.sleep(1)

stat = 0

data = ["S", "S", "S", "S"]

while True:
   cc=str(ser.readline())
   x = cc[2:][:-5]
   data = data[-3:]
   data.append(x)
   temp = "".join(data)
   if temp=="FFFF":
      t.send_rc_control(0,30,0,0)
      print("Quad goes Front")
      data = ["S", "S", "S", "S"]
      stat = 1
      time.sleep(3)
   elif temp=="BBBB":
      t.send_rc_control(0,-30,0,0)
      print("Quad goes Back")
      data = ["S", "S", "S", "S"]
      stat = 1
      time.sleep(3)
   elif temp=="RRRR":
      t.send_rc_control(-30,0,0,0)
      print("Quad goes Right")
      data = ["S", "S", "S", "S"]
      stat = 1
      time.sleep(3)
   elif temp=="LLLL":
      t.send_rc_control(30,0,0,0)
      print("Quad goes Left")
      data = ["S", "S", "S", "S"]
      stat = 1
      time.sleep(3)
   else:
      if stat == 1:
         t.send_rc_control(0,0,0,0)
         print("RC Stabilized")
         stat = 0
   if x=="F":
      print("Front")
   elif x=="B":
      print("Back")
   elif x=="R":
      print("Right")
   elif x=="L":
      print("Left")
   print("Stable")