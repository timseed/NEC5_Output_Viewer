# NEC5 Output Processing

**This repo does not, nor will it ever contain the NEC5 executables**. 

Please contact LLNL [https://www.llnl.gov/](https://www.llnl.gov/) to obtain your legal copy of NEC50. They are very easy to deal with, and the software is quite reasonably priced.

*Still working on some issues in this code base*


## Modelling

Despite having access to EZNec, 4Nec2 and MMANA - I wanted to see what the hype with NEC5 was about. So I got my NEC5 executables, it not only has an *engine* but a front end package ... which after 4 months I still could not understand. 

Hence this....

## NEC5 Files 

For a 'ham' you can start with thinking of the format of NEC5 as being the same as NEC2... 99% of people use 

  - GW
    - Wire definition
  - EX 
    - Where the RF power connects to the antenna
  - FR 
    - What frequency this is for 

So if that sounds like you then - NEC5 will not tax your brain. 

If however you have been using the most excellent **4nec2** for a while (as I have) - then you will be please to know that *Synbols*/*variables* are available in NEC5 - **but** I can not get them to work the same as 4NEC2

### Diplole using Synbols 

In 4nec2 you can use variable and do **maths** on them... this seems impossible in NEC5.
```4nec2 
CM Simple Diplot 
CE
SY Base=20	'Total Width
SY Z=30	        'Height of Centre
SY W=#14	'Gauge of Wire
SY S=101	'Segments
GW 1 Si -1*Base/2 0 Z Base/2 0 Z W 'Dipole line
GE 1
EX 0 1	51	0	1	0	0
FR	0	0	0	0	7.1	0
```

## NEC5 Gui 

No clue how it works... sometimes it does - sometimes it does not.
The *builder* seems very unforgiving - so much so I now just write the NEC files by hand. 

## Visualizing the NEC5 output

For me - via the GUI this does not work. I have tried using VM Windows, Bare-Metal windows machines - none work. But the*engine* does produce .OUT files. And so this is what I am now processing.

 
