from gpiozero import Servo,Button

door = Servo(26)
button_inside = Button(24)
button_outside = Button(5)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

try:
    while True :
        pir_state=GPIO.input(22)
        
        
        
        door.min()
        print("press the button")
        
        if pir_state == True :
            GPIO.output(17,True)
        else :
            GPIO.output(17,False)
            
        if button_inside.is_pressed or button_outside.is_pressed:
            #print(button1.value)
            #print(button.value)
            pir_state=GPIO.input(22)
            
        
            if button_outside.value==1 or (button_inside.value ==1 and pir_state==False ):
                door.max()
            else :
                print('Someone is at the outdoor')
        time.sleep(2)
                
            
        
except KeyboardInterrupt :
    GPIO.cleanup()
