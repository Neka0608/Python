from time import sleep     # Import sleep Library
import RPi.GPIO as GPIO    # Import GPIO Library 
GPIO.setmode(GPIO.BOARD)   # Use Physical Pin Numbering Scheme
button1=16                 # Button 1 is connected to physical pin 16
button2=12                 # Button 2 is connected to physical pin 12
button3=19
button4=36
LED1=22                    # LED 1 is connected to physical pin 22
LED2=18                    # LED 2 is connected to physical pin 18
LED3=11
LED4=15                     # LED 3 is connected to physical pin 23
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button1 an input, Activate Pull UP Resistor
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 2 an input, Activate Pull Up Resistor
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 3 an input, Activate Pull Up Resistor
GPIO.setup(button4,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button4 an input, Activate Pull UP Resistor
GPIO.setup(LED1,GPIO.OUT,) # Make LED 1 an Output
GPIO.setup(LED2,GPIO.OUT)  # Make LED 2 an Output
GPIO.setup(LED3,GPIO.OUT)  # Make LED 3 an Output
GPIO.setup(LED4,GPIO.OUT)  # Make LED 4 an Output


BS1=False                  # Set Flag BS1 to indicate LED is initially off
BS2=False
BS3=False
BS4=False

a=0                        # Set Flag BS2 to indicate LED is initially off
b=0
c=0
d=0
i=0
while(1):                  # Create an infinite Loop
        if GPIO.input(button1)==0:            # Look for button 1 press
                print ("Vote for RAMESH SIR")
                a=a+1
                print(a)
                if BS1==False:                # If the LED is off
                        GPIO.output(LED1,True)# turn it on
                        BS1=True# Set Flag to show LED1 is now On 
                        sleep(3)
                        GPIO.output(LED1,False)# Delay
                else:                         # If the LED is on
                        GPIO.output(LED1,False) # Turn LED off
                        BS1=False               # Set Flag to show LED1 is now Off
                        sleep(.5)             
        if GPIO.input(button2)==0: #Repeat above for LED 2 and button 2
                print ("Vote for GEETHA MAM")
                b=b+1
                print(b)
                if BS2==False:
                        GPIO.output(LED2,True) # turn it on
                        BS2=True# Set Flag to show LED2 is now On 
                        sleep(3)
                        GPIO.output(LED2,False)
                else:                         # If the LED is on
                        GPIO.output(LED2,False)# Turn LED off
                        BS2=False             # Set Flag to show LED1 is now Off
                        sleep(.5)
        if GPIO.input(button3)==0: #Repeat above for LED 3 and button 3
                print ("Vote for YOGESH SIR")
                c=c+1
                print(c)
                if BS3==False:
                        GPIO.output(LED3,True)# turn it on
                        BS3=True# Set Flag to show LED3 is now On 
                        sleep(3)
                        GPIO.output(LED3,False)
                else:
                        GPIO.output(LED3,False)
                        BS3=False
                        sleep(.5)
                        
        
        if GPIO.input(button4)==0: #Repeat above for LED 4 and button 4
                if BS4==False:
                        GPIO.output(LED4,True)# turn it on
                        BS4=True# Set Flag to show LED4 is now On 
                        sleep(3)
                        GPIO.output(LED4,False)
                        print ("RESULT")
                        if(a>b and a>c):
                                print("RAMESH SIR PARTY WIN",a)
                        elif(b>c):
                                print("GEETHA MAM PARTY WIN",b)
                        else:
                                print("YOGESH SIR PARTY WIN",c)
                else:
                        GPIO.output(LED4,False)
                        BS4=False
                        sleep(.5)
        


        


