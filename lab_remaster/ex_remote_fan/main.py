###################################
## Relay
##	> s: (BCM) #12
##	> +: 5.0V - Right 1st pin
##	> -: GND below #12 
##	> Com: Fan Moter Positive
##	> NO: 5.0V - Right 2nd pin
##
## Fan Motor
##	> +: Relay Com
##	> -: GND - Right 3rd pin
##################################
#!/usr/bin/env python
from devicehub.devicehub import Sensor, Actuator, Device, Project
import threading
from time import sleep
import RPi.GPIO as GPIO
import json
PROJECT_ID = '7233' #projekct_id
DEVICE_UUID = 'f95a6373-236b-4aeb-8736-e514f62a75e6' #device_uuid
API_KEY = '48b6d932-d36a-4879-93a6-9a63cdf52b7c' #api_key
ACTUATOR_NAME1 = 'fan_button' #do_button

GPIO.setmode(GPIO.BCM)

# init pin
fan = 12
GPIO.setup(fan, GPIO.OUT)

def fan_button(state):
	GPIO.output(fan, state)

def act1_callback(payload):
	"""
	:param payload: payload sent to actuator
	"""
	# handles message arrived on subscribed topic
	msg = str(payload)
	act_state = int(ACT1.state)
	if (act_state == 0):
		print "Signal Off received... do nothing"
	else:
		print "Signal On received... turn on the fan!!"
	fan_button(act_state)

project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)
ACT1 = Actuator(Actuator.DIGITAL, ACTUATOR_NAME1)
device.addActuator(ACT1, act1_callback)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
