class SmartPlug:    # Task 1
    def __init__(self, consumptionRate):
        self.consumptionRate = consumptionRate
        self.switchedOn = False

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
    
    def getSwitchedOn(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate
        
    def setConsumptionRate(self, rate):
        if rate <= 150 and rate >= 0:
            self.consumptionRate = rate
        else:
            errorMessage = "Rate is out of bounds."
            return errorMessage

    def __str__(self):
        output = f"Current consumption rate: {self.consumptionRate} | Switch 'ON' status: {self.switchedOn}"
        return output

# Testing SmartPlug
def testSmartPlug():
    mySmartPlug = SmartPlug(45)
    mySmartPlug.toggleSwitch()
    print(mySmartPlug.getSwitchedOn())
    print(mySmartPlug.getConsumptionRate())
    mySmartPlug.setConsumptionRate(77)
    print(mySmartPlug.getConsumptionRate())
    print(mySmartPlug)



# TEST RUN
testSmartPlug()