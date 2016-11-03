# Import libraries
import sys
import time
import RPi.GPIO as GPIO

#Using GPOI references instead of pins
GPIO.setmode(GPIO.BCM)

# Defining GPIO signals
# Pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [17,22,23,24]

# Set all pins as output
for pin in StepPins:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, False) #keeps it off

#sequence
Seq = [[1,0,1,0],[0,1,1,0],[0,1,0,1],[1,0,0,1]]

StepCount = len(Seq) #max length of sequence
StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

# Read wait time from command line
if len(sys.argv)>1: #if a time is given with the program
  WaitTime = int(sys.argv[1])/float(1000)

else: #if no time is given use this as defualt
  WaitTime = 10/float(1000)

# Initialise variables
StepCounter = 0 #so it will start at the first item in the list

# Start main loop
for number in range(int(sys.argv[2])): #Infinite loop

  #print StepCounter,
  #print Seq[StepCounter]

  for pin in range(0, 4): #creates an index so goes to 0-3
		xpin = StepPins[pin]

		if Seq[StepCounter][pin]== 1: #if it is 1 so turn on the pin
			#print " Enable GPIO %i" %(xpin)
			GPIO.output(xpin, True)
		else: #if it is 0 keep it off
			GPIO.output(xpin, False)

  StepCounter += StepDir #moves along one in sequence

  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
	StepCounter = 0
  if (StepCounter<0):
	StepCounter = StepCount+StepDir

  # Wait before moving on
  time.sleep(WaitTime)

GPIO.cleanup()
