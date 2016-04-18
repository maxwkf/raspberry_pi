import RPi.GPIO as GPIO
import time
import sys
sys.path.append("../passive_buzzer")
import passive_buzzer

targetPin = 16
ledPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(targetPin, GPIO.IN)

GPIO.setup(ledPin, GPIO.OUT)


#print "Before Setup"
#passive_buzzer.setup()
#time.sleep(5)
#print "After Setup"

buzzer_on = False

setup_buzzer = False


try:


	while True:
		
		if (buzzer_on == True):
			print "Buzzer ON"
		else:
			print "Buzzer OFF"


		print GPIO.input(targetPin)
		print buzzer_on
		print (GPIO.input(targetPin) == 1 and buzzer_on == False)

		if(GPIO.input(targetPin) == 1 and buzzer_on == False):
			if (setup_buzzer == False):
				passive_buzzer.setup()

			print "Water: Play Music >"
			buzzer_on = True
			passive_buzzer.loop()
		elif(buzzer_on == True):
			print "Dry  : Stop Music []"
			buzzer_on = False
			passive_buzzer.destroy()
		time.sleep(1)



#        while True:
#		if(GPIO.input(targetPin) ==1):
#			GPIO.output(ledPin, True)
#			print "Water is detected"
#		else:
#			GPIO.output(ledPin, False)
#			print "Dry~~~~~~~~~~~~~~"
#			
#		time.sleep(5)

except KeyboardInterrupt:
                GPIO.setup(ledPin, GPIO.IN)
                GPIO.cleanup()

#GPIO.cleanup()
