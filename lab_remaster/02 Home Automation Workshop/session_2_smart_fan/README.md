# Pre-requisition
[optional] Depends on your KANO OS.

We need to install **make**, **gcc**, **build-essential**, **python-dev**, **python-openssl** for the following instruction run.

```
sudo apt-get install make gcc build-essential python-dev python-openssl
```

# Download the pigpio.zip from [http://abyz.co.uk/](http://abyz.co.uk/)
```
wget http://abyz.co.uk/rpi/pigpio/pigpio.zip
```

Then need to unzip it and goes inside the PIGPIO directory.
```
unzip pigpio.zip
cd PIGPIO
```

# make install and setup
```
sudo make install
sudo python3 setup.py install
```

# Download the DHT22.py library
[optional] Then copy the DHT22.py from http://abyz.co.uk/ examples. In this repository, I have already included it to you.

# Run the pigpio daemon as a service
sudo pigpiod

# Download and run the program
[optional] Create cookieDHT22.py as the video stated in Reference, I have already included it to you.
sudo python cookieDHT22.py

# Reference
Video: [Raspberry Pi Tutorial 26 - GPIO DHT22 Digital Temperature + Humidity Sensor](https://www.youtube.com/watch?v=e1c1EwFHHss)
