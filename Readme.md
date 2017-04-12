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

The aim of this echOmod is to get the signal, and convert it to a digital output to the RPi. An older version using a [CA3306](/CA3306E/) can be found as well.

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

### Mounted... yeay!! To test =)

![](/images/20170412_231408.jpg)

### PCB yeay !!

![](/images/bomanz_pcb.png)

### Generation of gerbers for OSHPark

http://docs.oshpark.com/design-tools/kicad/generating-kicad-gerbers/

### Images!

![](/images/20170406_124914.jpg) for slow

![](/images/20170406_124950.jpg) for fast

## Discussions

### TODO

* Moving

### DONE

* KiCAD

### People

* A lot !

## License

### Bomanz 

The [echOmods project](https://github.com/kelu124/echomods) and its prototypes (so Bomanz) are open hardware, and working with open-hardware components.

Licensed under TAPR Open Hardware License (www.tapr.org/OHL)

Copyright Kelu124 (luc@echopen.org / kelu124@gmail.com ) 2015-2018

### Based on 

The following work is base on a previous TAPR project, [Murgen](https://github.com/kelu124/murgen-dev-kit) - and respects its TAPR license.

Copyright Kelu124 (murgen@echopen.org , luc@echopen.org / kelu124@gmail.com ) 2015-2018
