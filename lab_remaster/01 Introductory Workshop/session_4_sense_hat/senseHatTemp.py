import time
from sense_hat import SenseHat
sense=SenseHat()

e = [0, 0, 0]

image = [
e, e, e, e, e, e, e, e, 
e, e, e, e, e, e, e, e, 
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e, 
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e, 
e, e, e, e, e, e, e, e, 
e, e, e, e, e, e, e, e
] 
try: 
	while True:
		t = sense.get_temperature()
		h = sense.get_humidity()

		t=round(t, 1)
		h=round(h, 1)
	
		if t>30:
			bg = [100, 0, 0]
		else: 
			bg = [0,100, 0]

		msg = "Temperature = %s, Humidity = %s" %(t, h)
	
		print msg
		sense.show_message(msg, scroll_speed = 0.1, back_colour = bg)
	
		time.sleep(1)

except KeyboardInterrupt: 
	sense.set_pixels(image)
