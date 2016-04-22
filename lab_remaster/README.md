# Download the pigpio.zip from [http://abyz.co.uk/](http://abyz.co.uk/)
```
wget http://abyz.co.uk/rpi/pigpio/pigpio.zip
```
unzip pigpio.zip
cd PIGPIO

#sudo apt-get install make
#sudo apt-get install gcc
sudo apt-get install make gcc build-essential python-dev python-openssl


make
sudo make install
sudo python3 setup.py install


then copy the DHT22.py from http://abyz.co.uk/ examples

sudo pigpiod

create cookieDHT22.py
python cookieDHT22.py
