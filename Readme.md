# Module: A high speed ADC for the RaspberryPi

The board in red:

![](/images/20170717_205251.jpg)



## Description

### What is it supposed to do?

I've always needed a small upgrade to the existing raspberry ADC extensions, would love something in the 20-Msps range. Let's see if one can do it! Never tried smd, and thinking of using both smd and dip.. interesting learning curve ahead.

I've tried 3 different versions, increasing in complexity

* An older version using a [CA3306](/CA3306E/) can be found as well: going around 10Msps, 6 bits. DIP based components.
* A possibly [fast version of a 8 bit AD08200 ADC](/ADC08200/) is available, going up to 12Msps. 
* The latest [24Msps pHAT](/AD9200v2/)

### Image of these HATs

![](/images/20170717_203224.jpg)

## Some results

### 24 Msps with the latest version

Details and FFT of a signal at 1.9MHz

![](/images/twoadcs.jpg)

### 11 Msps with the previous

FFT of a signal at 1.9MHz

![](/images/ADC08200silentADCfft.png)

### Testing a 1MHz signal with the CA3306

Imaging a 1MHz sine:

![](/images/20170422-FirstAcqs.jpg)

![](/images/20170422-FirstAcqs-freq.png)
 
## License

### Bomanz 

The [echOmods project](https://github.com/kelu124/echomods) and its prototypes (so Bomanz) are open hardware, and working with open-hardware components.

Licensed under TAPR Open Hardware License (www.tapr.org/OHL)

Copyright Kelu124 (kelu124@gmail.com ) 2015-2018


