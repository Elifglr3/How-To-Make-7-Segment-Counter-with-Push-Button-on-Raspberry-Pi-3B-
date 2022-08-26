#Libraries
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
Button = 22
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT) # A
GPIO.setup(6, GPIO.OUT)  # B
GPIO.setup(16, GPIO.OUT) # C
GPIO.setup(20, GPIO.OUT) # D
GPIO.setup(21, GPIO.OUT) # E
GPIO.setup(19, GPIO.OUT) # F
GPIO.setup(26, GPIO.OUT) # G
    # String of characters storing PORT values for each digit
# Functions
# Reads a bit of a number
def bitRead(value, bit):
   return value & (1 << bit)  # shift mask to bit position and AND to value
# Resets counter and display to 0

# Assigning GPIO logic by taking 'pin' value

        
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def PORT(pin):
    if(pin&0x01 == 0x01):
        GPIO.output(13,1)            
    else:
        GPIO.output(13,0)            
    if(pin&0x02 == 0x02):
        GPIO.output(6,1)             
    else:
        GPIO.output(6,0)            
    if(pin&0x04 == 0x04):
        GPIO.output(16,1)
    else:
        GPIO.output(16,0)
    if(pin&0x08 == 0x08):
        GPIO.output(20,1)
    else:
        GPIO.output(20,0)   
    if(pin&0x10 == 0x10):
        GPIO.output(21,1)
    else:
        GPIO.output(21,0)
    if(pin&0x20 == 0x20):
        GPIO.output(19,1)
    else:
        GPIO.output(19,0)
    if(pin&0x40 == 0x40):
        GPIO.output(26,1)
    else:
        GPIO.output(26,0)
count=0
while True:
    dat = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F]
    button_state = GPIO.input(Button)
    if button_state == 1:
        count=count+1
        if count==10:
            count=0
        pin= dat[count]
        PORT(pin)
        sleep(0.5)
    else:
        sleep(1.0)
#def destroy():     
#        GPIO.cleanup()              

#if __name__ == '__main__':
#    setup()
#    try:
#        loop()
#    except KeyboardInterrupt:
#        print("Keyboard Interrupt Detected")
#        destroy()
