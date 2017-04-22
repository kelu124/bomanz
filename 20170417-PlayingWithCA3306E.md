# Log file

## Intro, references, ...

Original here: https://github.com/themagpimag/magpi-issue24/tree/master/PiScope .. and with [the copy of the txt](/CA3306E/code/piscope.txt).

.. even the original ... http://paul.sullivan.za.org/raspberry-pi-oscilloscope/EE-October-1991/

See http://www.instructables.com/id/PiScope-Raspberry-Pi-based-Oscilloscope/ - inspiration for the whole project. Heart of the build:
* CA3306 (6 bit parallel A/D converter IC) -- see [datasheet](/pdf/CA3306.pdf)
* TXB0108 (logic level converter IC) 

Note to self: [Bomanz on OSHPark](https://blog.oshpark.com/2017/04/15/high-speed-adc-phat-for-raspberry-pi/), yeay!!

### Biblio

- [x] PiScope on [MagPi24](https://github.com/themagpimag/magpi-issue24/tree/master/PiScope)
- [ ] Article from [Paul Sullivan](http://paul.sullivan.za.org/raspberry-pi-oscilloscope/)
- [x] Article from [EE Oct 1991](http://paul.sullivan.za.org/raspberry-pi-oscilloscope/EE-October-1991/)
- [ ] [Instructable ref doc](http://www.instructables.com/id/PiScope-Raspberry-Pi-based-Oscilloscope/ )
- [ ] [Info on DigiBird](https://digibird1.wordpress.com/raspberry-pi-as-an-oscilloscope-10-msps/): comments on noise from the GPIOs read
- [ ] [Explainations on the kernel and macros](http://www.pieter-jan.com/node/15)
- [ ] [Better input management](http://bobdavis321.blogspot.fr/2013/06/arduino-powered-3-million-samples-per.html)
- [ ] [ARduino clocking](http://www.nutsvolts.com/magazine/article/March2014_Davis	)

## 

### Preparing the RPi

See https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md for direct ssh

* Recommend activating Wifi, SSH, VNC beforehand
* note to self: __don't use rpi-update__ before.

### Cleaning the SD card

See this: http://raspi.tv/2016/how-to-free-up-some-space-on-your-raspbian-sd-card-remove-wolfram-libreoffice

```
sudo apt-get purge wolfram-engine wolfram-engine scratch minecraft-pi sonic-pi dillo gpicview penguinspuzzle oracle-java8-jdk openjdk-7-jre oracle-java7-jdk openjdk-8-jre chromium-browser libreoffice*
sudo apt-get remove 
sudo apt-get clean
sudo apt-get autoremove
```

If that's not enough, you can check the remaining packages by size:

```
dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -nr | more
```

### Installing

Following the steps:

* Run the [prepareModules.sh script](/CA3306E/code/prepareModules.sh)
* Prepare the module with [ca3306.c](/CA3306E/code/ca3306.c) and the corresponding [Makefile](/CA3306E/code/Makefile) ( `ca3306-drv.c` had a couple of bugs left ) 
* Compile with:

```
sudo make
```

One can obtain details on the module via:

```
modinfo ca3306.ko
```

```
sudo insmod ./ca3306.ko
```

Check with a dmesg where the Major of the chardev with a `dmesg`. Initial source was 248, in my case 243.. check yours =)

```
sudo mknod /dev/chardev c 243 0
```

The first compilation takes a while...

### Testing 


* Test with the [getSample.cpp](/CA3306E/code/getSample.cpp)

```
g++ -o getSample getSample.cpp
./getSample > [data.txt](/CA3306E/data/1MHz.data)
```

And finally we get, for an image of a 0-2V sine at 1MHz:

![](/images/20170422-FirstAcqs.png)

Not perfect, can be better, but at least we get something that goes fast =)

### More fun ?

* See the datasheet to increase the sampling frequency with a second ADC
* See how to increase by one bit


