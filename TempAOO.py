from machine import Pin
import time

led = Pin(25, Pin.OUT)
picoPin = Pin(15, Pin.OUT) #create picoPin at Pin 15, Set to output
pcOn = Pin(16, Pin.IN, Pin.PULL_DOWN)

def SwitchOn():
    if not pcOn.value():   #If PC is off
        picoPin.value(0)    #Set picoPin turn off
        time.sleep(1.0) #Maintain for 1s then continue
        
    else:
        print("PC ALREADY ON")
        

def SwitchOff():
    if pcOn.value():    #If PC is on
        picoPin.value(0)    #Set picoPin turn off
        time.sleep(5.0) #Maintain for 5s then continue
        
    else:
        print("PC ALREADY OFF")
        

try:
    while True:
        led.value(1)
        time.sleep(0.5)
        picoPin.value(1)    # Keep picoPin turn on
        now = time.localtime()
        timeNow = "{}:{}:{}".format(now[3], now[4], now[5])
        
        if timeNow == "22:0:0":
            SwitchOff()
           
        if timeNow == "6:0:0":
            SwitchOn()
            
        led.value(0)
        time.sleep(0.5)

except:
    pass
