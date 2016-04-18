import RPi.GPIO as GPIO
import time

targetPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(targetPin, GPIO.OUT)

try:
	while True:
		GPIO.output(targetPin, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(targetPin, GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
		GPIO.setup(targetPin, GPIO.IN)
		GPIO.cleanup()
	
