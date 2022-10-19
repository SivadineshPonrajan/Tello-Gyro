# Gesture controlled Quadcopter

In this project, I controlled the DJI's Tello quadcopter with the MPU6050 MEMS Sensor.

- Used the Arduino IDE to program the nodemcu microcontroller.
- Used ["djitellopy"](https://pypi.org/project/djitellopy/) python library to control the tello via its SDK.

## Working Explained

![Architecture](https://raw.githubusercontent.com/SivadineshPonrajan/Tello-Gyro/main/Images/Architecture.PNG)

- The Nodemcu reads the data from the MEMS and serially writes the data to the PC.
- The code for the Nodemcu can be found in the ["Tello_Gyro" directory](https://github.com/SivadineshPonrajan/Tello-Gyro/tree/main/Tello_Gyro).
- The python file ["GyroControl.py"](https://github.com/SivadineshPonrajan/Tello-Gyro/blob/main/GyroControl.py) reads the serial data and sends the commands to the Tello via sockets(UDP).
- The prerequisites are just the basic Nodemcu configuration in the Arduino IDE and the installation of the djitellopy python library.

> Note - The python code is optimised to run in the indoor/controlled environment.

> Check and change the serial port name in the code before you run the code.
