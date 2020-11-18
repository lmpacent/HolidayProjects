#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *

#Required for sleep statement
import time

#Create
power = DigitalOutput()

#Address
power.setIsHubPortDevice(True)
power.setHubPort(0)

#Open
power.openWaitForAttachment(5000)

#Use your Phidgets
while(True):
    #get local hour
    localHour = time.localtime()[3]
    #if it is after 5pm and before midnight, turn on the tree/decorations
    if(localHour >= 17 and localHour <= 23):
        power.setState(True)
    else:
        power.setState(False)        
    time.sleep(30)
  
