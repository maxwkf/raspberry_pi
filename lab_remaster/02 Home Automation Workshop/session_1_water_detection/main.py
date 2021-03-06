###################################
## Water Sensor
## 	> S: (BCM) #4
##	> +: 3.3V - Left 1st pin
##	> -: GND below #4
##
## Passive Buzzer
## 	> S: (BCM) #18
##	> +: 5.0V - Right 1st pin
##	> -: GND - Right 3rd pin
##################################
import RPi.GPIO as GPIO
import time

waterPin = 4
buzzerPin = 18

setup_buzzer = False
buzzer_on = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(waterPin, GPIO.IN)

CL = [0, 131, 147, 165, 175, 196, 211, 248]		# Frequency of Low C notes

CM = [0, 262, 294, 330, 350, 393, 441, 495]		# Frequency of Middle C notes

CH = [0, 525, 589, 661, 700, 786, 882, 990]		# Frequency of High C notes

song_1 = [	CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6], # Notes of song1
			CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3], 
			CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
			CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]	]

beat_1 = [	1, 1, 3, 1, 1, 3, 1, 1, 			# Beats of song 1, 1 means 1/8 beats
			1, 1, 1, 1, 1, 1, 3, 1, 
			1, 3, 1, 1, 1, 1, 1, 1, 
			1, 2, 1, 1, 1, 1, 1, 1, 
			1, 1, 3	]

song_2 = [	CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1], # Notes of song2
			CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2], 
			CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1], 
			CM[3], CM[2], CL[5], CL[7], CM[2], CM[1]	]

beat_2 = [	1, 1, 2, 2, 1, 1, 2, 2, 			# Beats of song 2, 1 means 1/8 beats
			1, 1, 2, 2, 1, 1, 3, 1, 
			1, 2, 2, 1, 1, 2, 2, 1, 
			1, 2, 2, 1, 1, 3 ]

def setup():
	GPIO.setmode(GPIO.BCM)		# Numbers GPIOs by physical location
	GPIO.setup(buzzerPin, GPIO.OUT)	# Set pins' mode is output
	global Buzz						# Assign a global variable to replace GPIO.PWM 
	Buzz = GPIO.PWM(buzzerPin, 440)	# 440 is initial frequency.
	Buzz.start(50)					# Start buzzerPin pin with 50% duty ration

def destory():
		Buzz.stop()									 # Stop the buzzer
		GPIO.output(buzzerPin, 1)		  # Set buzzerPin pin to High
		GPIO.cleanup()						  # Release resource


def loop():
	while True:
		print '\n	Playing song 1...'
		for i in range(1, 4):		# Play song 1
			Buzz.ChangeFrequency(song_1[i])	# Change the frequency along the song note
			time.sleep(beat_1[i] * 0.5)		# delay a note for beat * 0.5s
		time.sleep(1)						# Wait a second for next song.
		print "Before Break"
		if(GPIO.input(waterPin) == 0):
			print "Breaking"
			break
		

try:
	print "Program started. Waiting for water detection..."
	while True:
		if(GPIO.input(waterPin) == 1 and buzzer_on == False):
			if (setup_buzzer == False):
				setup()
				setup_buzzer = True
			print "Water detected: Play Music"
			buzzer_on = True
			loop()
		elif(buzzer_on == True):
			print "Dry  : Stop Music"
			buzzer_on = False
			destory()
			setup_buzzer = False
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(waterPin, GPIO.IN)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
