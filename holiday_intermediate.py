#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Net import *
from Phidget22.Devices.Dictionary import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.HumiditySensor import *

#Required for sleep statement
import time

#variable used for updates
scheduleSet = True

#dictionary update event
def onUpdate(self, key, value):
    print(key + " " + value)
    if(key == "powerSet"):
        if(value == "true"):
            power.setState(True)
        else:
            power.setState(False)
        
    elif(key == "scheduleSet"):
        global scheduleSet
        if(value == "true"):
            scheduleSet = True
        else:
            scheduleSet = False
    
#enable network discovery for dictionary
Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)

#Create
power = DigitalOutput()
phid_dict = Dictionary()
temp = TemperatureSensor()
hum = HumiditySensor()


#Address
power.setIsHubPortDevice(True)
power.setHubPort(0)
phid_dict.setDeviceSerialNumber(1002)

#events
phid_dict.setOnUpdateHandler(onUpdate)

#Open
power.openWaitForAttachment(5000)
phid_dict.openWaitForAttachment(5000)
temp.openWaitForAttachment(5000)
hum.openWaitForAttachment(5000)

#update Dictionary with starting parameters
phid_dict.set("powerSet", "false")
phid_dict.set("scheduleSet", "true")

#Use your Phidgets
while(True):
    phid_dict.set("humidity",str(hum.getHumidity()))
    phid_dict.set("temperature",str(temp.getTemperature()))
    
    if(scheduleSet):
        localHour = time.localtime()[3]
        if(localHour >= 11 and localHour <= 23):
            power.setState(True)
        else:
            power.setState(False)        
    time.sleep(30)
  
