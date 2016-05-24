###################################
## Temperature Sensor
## 	> S: (BCM) #19
##	> +: (BCM) #26
##	> -: GND next to #26
##
## Relay
##	> s: (BCM) #12
##	> +: 3.3V - Left 1st pin
##	> -: GND below #18
##	> Com: Fan Moter Positive
##	> NO: 3.3V - Below #22
##
## Fan Motor
##	> +: Relay Com
##	> -: GND - Right 3rd pin
##################################
import sys
import pigpio
import DHT22
from time import sleep

# get the parameters
argNames = ['filename', 'temperature']
args = dict(zip(argNames, sys.argv))

# setting some default values, Pin # using BGM
sensorPin = 19
sensorVoltagePin = 26
targetOutputPin = 12	# this is the pin giving signal to relay -> fan motor
sleepTime = 3
targetTemperature = int(args['temperature'])	# getting the input from argv

pi = pigpio.pi()
# turn on the sensor
pi.set_mode(sensorVoltagePin, pigpio.OUTPUT)
pi.write(sensorVoltagePin, True)
# setup the DHT22 sensor pin
dht22 = DHT22.sensor(pi, sensorPin)
# setup the relay -> fan motor output pin
pi.set_mode(targetOutputPin, pigpio.OUTPUT)

# defined how to read the DHT22
def readDHT22():
	dht22.trigger()
	humidity = '%.2f' % (dht22.humidity())
	temp = '%.2f' % (dht22.temperature())
	return (float(humidity), float(temp))

# the core program run
try:
	print("[Please use Ctrl + C to termate the program]\n")
	print("Program Start...")
	print("When the temperature is HIGHER then " + str(targetTemperature) + ". The relay -> fan motor will turn on!\n")
	while True:
		humidity, temperature = readDHT22()
		if (temperature > targetTemperature):
			pi.write(targetOutputPin, True)
		else:
			pi.write(targetOutputPin, False)
		print("Temperature is: " + str(temperature) + "C    Humidity is: " + str(humidity) + "%")
		sleep(sleepTime)
		
except KeyboardInterrupt:
	pi.set_mode(targetOutputPin, pigpio.INPUT)
	pi.set_mode(sensorVoltagePin, pigpio.INPUT)
	print("/Program Stop...")
