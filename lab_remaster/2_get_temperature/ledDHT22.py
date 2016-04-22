import sys
import pigpio
import DHT22
from time import sleep

# setting some default values, Pin # using BGM
sensorPin = 18
sensorVoltagePin = 17
ledPin = 23
sleepTime = 3
targetTemperature = int(sys.argv[1])	# getting the input from argv

pi = pigpio.pi()
# turn on the sensor
pi.set_mode(sensorVoltagePin, pigpio.OUTPUT)
pi.write(sensorVoltagePin, True)
# setup the DHT22 sensor pin
dht22 = DHT22.sensor(pi, sensorPin)
# setup the LED output pin
pi.set_mode(ledPin, pigpio.OUTPUT)

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
			pi.write(ledPin, True)
		else:
			pi.write(ledPin, False)
		print("Temperature is: " + str(temperature) + "C    Humidity is: " + str(humidity) + "%")
		sleep(sleepTime)
except KeyboardInterrupt:
	print("/Program Stop...")
