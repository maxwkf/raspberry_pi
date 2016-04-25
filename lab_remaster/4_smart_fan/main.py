import sys
import pigpio
import DHT22
from time import sleep

# get the parameters
argNames = ['filename', 'temperature']
args = dict(zip(argNames, sys.argv))

# setting some default values, Pin # using BGM
sensorPin = 18
sensorVoltagePin = 17
targetOutputPin = 23	# this is the pin giving signal to the relay, then to the fan
sleepTime = 3
targetTemperature = int(args['temperature'])	# getting the input from argv

pi = pigpio.pi()
# turn on the sensor
pi.set_mode(sensorVoltagePin, pigpio.OUTPUT)
pi.write(sensorVoltagePin, True)
# setup the DHT22 sensor pin
dht22 = DHT22.sensor(pi, sensorPin)
# setup the LED output pin
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
	print("When the temperature is HIGHER then " + str(targetTemperature) + ". The LED will turn on!\n")
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
