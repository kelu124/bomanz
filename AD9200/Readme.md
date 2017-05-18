# Going into this 20Msps to 40Msps pHAT  for Raspberry Pi

## Problem and solution

__Problem__ was that the Pi0 or PiW, with the current kernel module, can't run faster than around 10 to 12 Msps. Clock can be faster, but the _memcpy_ limits the transfer to memory. Soooo.. what can we do? As a reminder, I wanted at least a 10Msps 10bit ADC.

__Solution__ Why not interleaving two ADCs, with clocks in opposite phase? Hum that means 2 times 10 bits, and I had only 18 pins left once the Ultrasound SDK board connected. That means.. quite obviously, 2 times 9 bits.

So now I can run at twice the speed of the transfer, so a bit over 20Msps, over this time 9 bits. Or by oversampling, that could be 10Msps at 10 bits. __With more flexibility__ !

Win.

At least for the moment, now I need to order the PCBs and some components.

-> BOM is around 30$ components, 5$ OSHPark PCB.. that's quite neat.


## What does it look like?


#### Top in 3D

![](/AD9200/top-3d.png)

#### Bottom in 3D

![](/AD9200/bot-3d.png)
