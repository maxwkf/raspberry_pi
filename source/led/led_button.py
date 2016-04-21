#!/usr/bin/env python
from devicehub.devicehub import Sensor, Actuator, Device, Project
import threading
from time import sleep
import RPi.GPIO as GPIO
import json
PROJECT_ID = '6898' #projekct_id
DEVICE_UUID = 'e615f24b-79ea-4526-abe4-f98acbf41c34' #device_uuid
API_KEY = '1202a342-6b2c-4943-b783-338593ad4f56' #api_key
ACTUATOR_NAME1 = 'led_button' #do_button

# init pin
led = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

def led_button(state):
	GPIO.output(led, state)
	print " state: ", state

def act1_callback(payload):
	"""
	:param payload: payload sent to actuator
	"""
	# handles message arrived on subscribed topic
	msg = str(payload)
	act_state = ACT1.state
	print "act1", act_state
	led_button(act_state)

project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)
ACT1 = Actuator(Actuator.DIGITAL, ACTUATOR_NAME1)
device.addActuator(ACT1, act1_callback)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
