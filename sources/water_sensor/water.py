import RPi.GPIO as GPIO
import time

targetPin = 16
ledPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(targetPin, GPIO.IN)

GPIO.setup(ledPin, GPIO.OUT)

try:
        while True:
		if(GPIO.input(targetPin) ==1):
			GPIO.output(ledPin, True)
			print "Water is detected"
		else:
			GPIO.output(ledPin, False)
			print "Dry~~~~~~~~~~~~~~"
			
		time.sleep(5)

except KeyboardInterrupt:
                GPIO.setup(ledPin, GPIO.IN)
                GPIO.cleanup()

#GPIO.cleanup()
