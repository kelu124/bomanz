# Log file

## Intro, references, ...

Original here: https://github.com/themagpimag/magpi-issue24/tree/master/PiScope .. and with [the copy of the txt](/CA3306E/code/piscope.txt).

.. even the original ... http://paul.sullivan.za.org/raspberry-pi-oscilloscope/EE-October-1991/

See http://www.instructables.com/id/PiScope-Raspberry-Pi-based-Oscilloscope/ - inspiration for the whole project. Heart of the build:
* CA3306 (6 bit parallel A/D converter IC)
* TXB0108 (logic level converter IC) 

Note to self: [Bomanz on OSHPark](https://blog.oshpark.com/2017/04/15/high-speed-adc-phat-for-raspberry-pi/), yeay!!

## 

### Cleaning the SD card

See this: http://raspi.tv/2016/how-to-free-up-some-space-on-your-raspbian-sd-card-remove-wolfram-libreoffice

```
sudo apt-get purge wolfram-engine
sudo apt-get remove --purge libreoffice*
sudo apt-get remove wolfram-engine scratch minecraft-pi sonic-pi dillo gpicview penguinspuzzle oracle-java8-jdk openjdk-7-jre oracle-java7-jdk openjdk-8-jre chromium-browser
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
* Prepare the module with [ca3306-drv.c](/CA3306E/code/ca3306-drv.c) and the corresponding [Makefile.sh](/CA3306E/code/Makefile.sh)
* Compile with:

```
sudo make
```

One can obtain details on the module via:

```
modinfo ca3306-drv.ko
```

```
sudo insmod ./ca3306-drv.ko
sudo mknod /dev/chardev c 248 0
```

The first compilation takes a while...

### Testing 

* Test with the [readout.cpp](/CA3306E/code/readout.cpp)

```
g++ -o readout readout.cpp
./readout > data.txt
```

### 

```
sudo apt-get install -y gnuplot-x11 
```


