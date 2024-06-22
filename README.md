# Making a Touch Directory
The hardware/software interface of a touch directory

*The direct purpose of this is to record my trial and error to help others (and myself) in the future.*
*Esp the helpdesk*

## Hardware
I am using a mini-PC and a touch enabled TV

## Software
I have tried this on a couple different operating systems 

### Ubuntu
I am ensuring that I have `wget`, `firefox`, and I will again wirte a couple simple scripts
- I am now scpapping the wget idea and now
- now i am writing 2 different python files
-   one to restart the computer `restart.py` one lauch the webpage `directory.py`
-   restart import os
-   directory import webbrowser
-     `--fullscreen`, `--kiosk` ... I am not sure this will work but ill try on monday
- then i will use `chron` to schedual the python scripts to run 

### Windows 10
Windows 10 worked great!
I was able to make this work smoothly with a couple simple steps.

- ensuring a simple uninterupted login
- a simple bash script to restart the computer
- a schortcut to the desired website
-    I used Firefox because of the ease I had at adding the `--kiosk` and `--fullscreen` arguments into the desktop shortcut and the taskscheduler 

### Windows 11
This is where the weels fell off (again).

Because of the secutiry features in windows 11 it made an automatic login difficult.

Because of the domain protocols of where I am working Windows 11 Kiosk mode was not a viable option. although otherwise this would be a great way to implament this.
So This is why I turned to Linux
