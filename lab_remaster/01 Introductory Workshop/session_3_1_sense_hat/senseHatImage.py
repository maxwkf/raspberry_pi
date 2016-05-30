import time
from sense_hat import SenseHat

sense = SenseHat()

e = [0, 0, 0] #off
w = [150, 150, 150] #white
g = [0, 255, 0]
r = [255, 0, 0]
b = [0, 0, 255]
o = [255, 127, 0]
y = [255, 255, 0]
v = [ 159, 0, 255]

default = [
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e, 
e, e, e, e, e, e, e, e, 
e, e, e, e, e, e, e, e
]

smile = [
e, e, e, e, e, e, e, e,
e, e, v, e, e, y, e, e, 
e, e, r, e, e, w, e, e, 
e, e, g, e, e, o, e, e, 
e, e, e, e, e, e, e, e, 
e, w, e, e, e, e, y, e, 
e, b, e, e, e, e, o, e, 
e, w, g, r, b, o, y, e,
]

try: 
	while True: 
		sense.set_pixels(smile)
		time.sleep(3)	
		sense.show_message("CS", text_colour = o)

except KeyboardInterrupt:
	sense.set_pixels(default)
