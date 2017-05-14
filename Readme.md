# Module: Bomanz [](@description Bomanz description)

![](/images/bomanz_pcb.png)

## Name

[`MDL-bomanz_ADC08200`]()


## Title

Bomanz: a high speed extension for Raspberry Pi

## Description

* Up to 200Msps
* version: V0.1
* date: 20/04/2017
* cost:40$
* sourcing:Custom made, get the [Kicad FIles](/source/kicad/)  or contact @kelu124
* technology: pHat, ICs based on `ADC08200`
* language: Kicad
* author: Kelu124

## IOs

### Inputs

* `ITF-A_gnd`
* `ITF-B_5v`
* `ITF-S_3_3v`

### Outputs

* `ITF-mEG_RPi` : signal from the ADC to thge RPi

## Key Components

* `ADC08200`: 200Msps ADC  

## Information

### What is it supposed to do?

I've always needed a small upgrade to the existing raspberry ADC extensions, would love something in the 20-Msps range. Let's see if one can do it! Never tried smd, and thinking of using both smd and dip.. interesting learning curve ahead.

 An older version using a [CA3306](/CA3306E/) can be found as well.

### How does it work: block diagram

![Block schema](/source/blocks.png)

* `ITF-C_amplified_raw_signal`->`4-Square, D-72`->`SOD-123`->`ADC08200`->`RPi0`
* `ITF-E_signal_envelope`->`4-Square, D-72`

## About the module

### Pros

* Only needs 5V and 3.3V inputs.
* ADC is quick
* 

### Cons: what to to make better

* To be tested

 
## Constraint and limits

### ADC08200 captures.. it works too!

#### Signals? 

Managed to get the signals from the [emulator](https://github.com/kelu124/echomods/tree/master/silent/).

![](/images/SilentSigs.jpg)

There's room enough to play with FFTs =) Let's see what FFT can yield on peaks from a 3.5MHz piezo ?

![](/images/ADC08200piezoFFTed.png)

#### Comparing to Croaker

Let's now compare the acquisition to the [STM32 DAQ](https://github.com/kelu124/echomods/tree/master/croaker/).

![](/images/BomanzVSCroaker.png)

### CA3306 captures.. it works!

See the [worklog in jupyter](/CA3306E/20170422-FirstAcqs.ipynb) for the [CA3306E (see datasheet)](/pdf/CA3306.pdf)

![](/images/20170422-FirstAcqs.png)

Image of a 0-2V sine at 1MHz.


### Compiling...

See the [20170417-PlayingWithCA3306E worklog](/20170417-PlayingWithCA3306E.md)

### Mounted... yeay!! To test =)

![](/images/20170412_231408.jpg)

**Note to self**: Tantalum capacitor: not in reverse! Never!!

### PCB yeay !!

![](/images/bomanz_pcb.png)

### Generation of gerbers for OSHPark

http://docs.oshpark.com/design-tools/kicad/generating-kicad-gerbers/

### Images!

![](/images/20170406_124914.jpg) for slow

![](/images/20170406_124950.jpg) for fast

## Discussions

### TODO

* EndGame: moving to a 20-30Msps, for a 10 to 12 bit ADC. 
* Have access points to VRef, GND, and maybe VRef / 2 for self testing.
* Add reference voltage ICs to stabilize Vref
* Using another ADC
* See `TASK_UNINTERUPTIBLE` 

### DONE

* KiCAD

### People

* Thanks to @eiffel for his kernel expertise and GPL3 crusade

 

## License

### Bomanz 

The [echOmods project](https://github.com/kelu124/echomods) and its prototypes (so Bomanz) are open hardware, and working with open-hardware components.

Licensed under TAPR Open Hardware License (www.tapr.org/OHL)

Copyright Kelu124 (luc@echopen.org / kelu124@gmail.com ) 2015-2018

### Based on 

The following work is base on a previous TAPR project, [Murgen](https://github.com/kelu124/murgen-dev-kit) - and respects its TAPR license.

Copyright Kelu124 (murgen@echopen.org , luc@echopen.org / kelu124@gmail.com ) 2015-2018
