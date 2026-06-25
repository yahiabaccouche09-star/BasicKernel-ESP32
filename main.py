#  BasicKernel - An embedded OS for microcontrollers using MicroPython
#  Copyright (C) 2026  Yahia Baccouche
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
print("Starting...")
import machine
from machine import Pin, time_pulse_us, freq
from time import sleep, sleep_us

tem = Pin(13, Pin.OUT)
tem.value(1)

def ultrason(trig, echo):
    trig.value(1)
    sleep_us(10)
    trig.value(0)
    duration = time_pulse_us(echo, 1, 30000)
    dist = (duration * 0.0343) / 2
    if dist > 0:
        return dist
    else:
        return "out of range"

def pir(pinpir):
    if pinpir.value() == 1:
        return "someone is there"
    elif pinpir.value() == 0:
        return "no one is there"

print("""
*********************************
          basic kernel
           build 1.00
*********************************""")

trig = int(input("trig pin: "))
echo = int(input("echo pin: "))
pinpir = int(input("pir pin: "))
print("Configuring components...")

p = Pin(pinpir, Pin.IN)
t = Pin(trig, Pin.OUT)
e = Pin(echo, Pin.IN)
print("Devices detected!")

while True:
    com = str(input(">_"))
    
    if com == "help":
        print("""
----------------------------------------------------------------
                        Available commands:
    dist-->display the distance measured by the ultrasonic sensor
    pirchck-->check the PIR sensor status
    help-->help menu
    restart-->reboot the microcontroller
    shutdown-->stop the microcontroller (deepsleep)
    about-->software information 
----------------------------------------------------------------
""")
    elif com == "dist":
        print(ultrason(t, e))
    elif com == "pirchck":
        print(pir(p))
    elif com == "restart":
        print("Rebooting microcontroller...")
        machine.reset()
    elif com == "shutdown":
        print("Microcontroller is shutting down...")
        machine.deepsleep()
    elif com == "about":
        print("""
---------------------------------
developer: yahia
system: BasicKernel for esp32
version: 1 (build 1.00)
---------------------------------
""")
    else:
        print(f"Command '{com}' is unknown")