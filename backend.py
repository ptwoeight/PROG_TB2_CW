class SmartPlug:    # Task 1
    def __init__(self, consumptionRate):
        self.consumptionRate = consumptionRate
        self.switchedOn = False
    
    def getSwitchedOn(self):
        return self.switchedOn
    
    def getConsumptionRate(self):
        return self.consumptionRate

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
        
    def setConsumptionRate(self, rate):
        #if rate <= 150 and rate >= 0:
        self.consumptionRate = rate
        #else:
            #errorMessage = "Rate is out of bounds."    # ^^ means no error messages here ^^
            #return errorMessage

    def __str__(self):
        output = f"Current consumption rate: {self.consumptionRate}  |  Status: "
        if self.getSwitchedOn(): 
            output += f"ACTIVE."
        else: 
            output += f"INACTIVE."
        return output 


class SmartTV:    # Task 2
    def __init__(self):
        self.switchedOn = False
        self.channel = 1

    def getSwitchedOn(self):
        return self.switchedOn

    def getChannel(self):
        return self.channel

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def setChannel(self, channel):
        if channel <= 175 and channel >= 1:
            self.channel = channel
        else: 
            errorMessage = "Channel does not exist."
            return errorMessage

    def __str__(self):
        output = f"Current channel: {self.channel}  |  Status: "
        if self.getSwitchedOn(): 
            output += f"ACTIVE."
        else: 
            output += f"INACTIVE."
        return output    


class SmartHome:    # Task 3 - this apparently needs a delete function coz they forgot to put that in the CW smh
    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices
    
    def getDeviceAt(self, index):
        return self.devices[index]
    
    def removeDeviceAt(self, index):
        if index < len(self.devices):
            self.devices.remove(self.devices[index])
    
    def addDevice(self, device):
        self.devices.append(device)
    
    def toggleSwitch(self, index):
        self.devices[index].toggleSwitch()      # we can use toggle switch coz the devices we're appending onto the list is of the SmartTV or SmartPlug class ! 

    def turnOnAll(self):
        if not self.devices:
            errorMessage = "There are no devices in your Smart Home."
            return errorMessage
        else:
            count = 0
            for device in self.devices:
                if self.devices[count].getSwitchedOn() == False:
                    self.devices[count].toggleSwitch()
                    count += 1
                else:
                    count += 1
                    continue

    def turnOffAll(self):
        if not self.devices:
            errorMessage = "There are no devices in your Smart Home."
            return errorMessage
        else:
            count = 0
            for device in self.devices:
                if self.devices[count].getSwitchedOn() == True:
                    self.devices[count].toggleSwitch()
                    count += 1
                else:
                    count += 1
                    continue

    def __str__(self):
        if not self.devices:
            errorMessage = "There are no devices in your Smart Home."
            return errorMessage
        else:
            output = f"Devices:"
            for device in self.devices:
                output += f"\n> {self.devices.index(device) + 1} - {device.__class__.__name__}: [{device.__str__()}]"
            return output


def testSmartPlug():    # Testing SmartPlug
    mySmartPlug = SmartPlug(45)
    mySmartPlug.toggleSwitch()

    print(mySmartPlug.getSwitchedOn())
    print(mySmartPlug.getConsumptionRate())
    mySmartPlug.setConsumptionRate(77)
    print(mySmartPlug.getConsumptionRate())
    print(mySmartPlug)

def testSmartTV():    # Testing SmartTV
    mySmartTV = SmartTV()
    mySmartTV.toggleSwitch()

    print(mySmartTV.getSwitchedOn())
    print(mySmartTV.getChannel())
    mySmartTV.setChannel(77)
    print(mySmartTV.getChannel())
    print(mySmartTV)

def testSmartHome():    #Testing SmartHome
    mySmartHome = SmartHome()
    smartPlugTest1 = SmartPlug(45)
    smartPlugTest2 = SmartPlug(45)
    mySmartTV = SmartTV()

    # devices
    smartPlugTest1.toggleSwitch()
    smartPlugTest1.setConsumptionRate(150)
    smartPlugTest2.setConsumptionRate(25)
    mySmartTV.setChannel(77)

    mySmartHome.addDevice(smartPlugTest1)   # on - TRUE
    mySmartHome.addDevice(smartPlugTest2)   # off - FALSE
    mySmartHome.addDevice(mySmartTV)    #off - FALSE

    mySmartHome.toggleSwitch(1)     # should be smartPlugTest2 toggled to turn it on

    print(mySmartHome)

    mySmartHome.turnOnAll()

    print(mySmartHome)

    mySmartHome.removeDeviceAt(0)

    print(mySmartHome)


# TEST RUN
testSmartHome()