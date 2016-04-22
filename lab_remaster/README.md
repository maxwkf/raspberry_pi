# Pre-requisition
[optional] Depends on your KANO OS.

We need to install **make**, **gcc**, **build-essential**, **python-dev**, **python-openssl** for the following instruction run.

<code>sudo apt-get install make
sudo apt-get install gcc
sudo apt-get install make gcc build-essential python-dev python-openssl</code>

# Download the pigpio.zip from [http://abyz.co.uk/](http://abyz.co.uk/)
<code>wget http://abyz.co.uk/rpi/pigpio/pigpio.zip</code>
Then need to unzip it and goes inside the PIGPIO directory.
<code>unzip pigpio.zip
cd PIGPIO</code>

# make install and setup
<code>make
sudo make install
sudo python3 setup.py install</code>

# Download the DHT22.py library
then copy the DHT22.py from http://abyz.co.uk/ examples

# Run the pigpio daemon as a service
sudo pigpiod

# Download and run the program
create cookieDHT22.py
python cookieDHT22.py
