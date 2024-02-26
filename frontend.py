from backend import SmartPlug, SmartTV, SmartHome
from tkinter import *

class SmartHomeSystem:
    def __init__(self, smartHome):
        self.smartHome = smartHome
        self.win = Tk()
        self.win.title("Smart Home System")
        self.win.geometry("675x275")
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(padx=15, pady=15)
        self.devices = self.smartHome.getDevices()

    def runWindow(self):
        self.deviceLabelFormat()
        self.createWidgets()
        self.win.mainloop()
    
    def deviceLabelFormat(self):
        self.messages = []

        for device in self.devices:
            if isinstance(device, SmartPlug):
                output = f"{device.__class__.__name__}: "
                if device.getSwitchedOn():
                    output += "ON | "
                else:
                    output += "OFF | "
                output += f"Consumption Rate: {device.getConsumptionRate()}"
                self.messages.append(output)
            else:
                output = f"{device.__class__.__name__}: "
                if device.getSwitchedOn():
                    output += "ON | "
                else:
                    output += "OFF | "
                output += f"Channel: {device.getChannel()}"
                self.messages.append(output)

    def createWidgets(self): # separate this with two methods: createbuttons, createdevicelabels
        self.listOfWidgets = []
        self.createButtons()
        self.createLabels()
        
    def createButtons(self):
        btnTurnOnAll = Button(
            self.mainFrame,
            text="Turn on all",
            width=30,
            borderwidth=5,
            command=self.turnOnAllButton
        )
        btnTurnOnAll.grid(column=0, row=0, sticky=W)

        btnTurnOffAll = Button(
            self.mainFrame,
            text="Turn off all",
            width=30,
            borderwidth=5,
            command=self.turnOffAllButton
        )
        btnTurnOffAll.grid(column=1, row=0, columnspan=2, sticky=W)

        for i in range(len(self.devices)):
            btnToggle = Button(
                self.mainFrame,
                text="Toggle",
                width=15,
                borderwidth=5,
                command= lambda index=i: self.toggleButton(index)
            )   
            btnToggle.grid(column=1, row=i+1, sticky=W)

        for i in range(len(self.devices)):
            btnEdit = Button(
                self.mainFrame,
                text="Edit",
                width=10,
                borderwidth=5
            )
            btnEdit.grid(column=2, row=i+1, sticky=W)

        for i in range(len(self.devices)):
            btnDelete = Button(
                self.mainFrame,
                text="Delete",
                width=15,
                borderwidth=5
            )
            btnDelete.grid(column=3, row=i+1, sticky=W)

        btnAddDevice = Button(
            self.mainFrame,
            text="Add",
            width=25,
            borderwidth=5,
            command=self.addButton
        )
        btnAddDevice.grid(column=0, row=6, sticky=W)

    def createLabels(self):
        # label
        for i in range(len(self.devices)):
            lblDevice = Label(
                self.mainFrame,
                text=self.messages[i]
            )
            lblDevice.grid(column=0, row=i+1, sticky=W)
            self.listOfWidgets.append(lblDevice)
            
    def turnOnAllButton(self):
        self.smartHome.turnOnAll()
        self.deviceLabelFormat()
        self.createLabels()
    
    def turnOffAllButton(self):
        self.smartHome.turnOffAll()
        self.deviceLabelFormat()
        self.createLabels()

    def toggleButton(self, index):
        self.smartHome.toggleSwitch(index)
        self.deviceLabelFormat()
        self.createLabels()
    
    def addButton(self):
        newDeviceWindow = Tk()
        newDeviceWindow.title("Add New Device")
        newDeviceWindow.geometry("200x100")
        mainFrame = Frame(newDeviceWindow)
        mainFrame.pack(padx=10, pady=10)
        mainFrame.pack()

        lblDevicePrompt = Label(
            mainFrame,
            text="Choose a device:"
        )
        lblDevicePrompt.pack()

        btnSmartPlugOption = Button(
            mainFrame,
            text="Smart Plug"
            
        )
        btnSmartPlugOption.pack(side="left")

        btnSmartTVOption = Button(
            mainFrame,
            text="Smart TV"
        )
        btnSmartTVOption.pack(side="right")

        newDeviceWindow.mainloop()

    







def setUpHome():
    finalDevices = []

    prompt = "Choose up to 5 devices for your Smart Home:\n[1] Smart Plug\n[2] Smart TV\n-"
    print(prompt)

    while len(finalDevices) < 5:
        userInput = input(f"Chosen Option: ")

        if userInput == "1" or userInput.lower() == "smart plug":
            invalidConsumptionRate = True

            while invalidConsumptionRate:
                inputConsumptionRate = input("Enter Consumption Rate: ")   # do try catch for TypeError

                while not inputConsumptionRate.isdigit():
                    print("Value entered is not an integer.")
                    inputConsumptionRate = input("Enter Consumption Rate: ")

                consumptionRateAsInt = int(inputConsumptionRate)

                if consumptionRateAsInt <= 150 and consumptionRateAsInt >= 0:
                    finalDevices.append(SmartPlug(consumptionRateAsInt))    
                    print("'Smart Plug' device added!")

                    invalidConsumptionRate = False
                else:
                    print("Value entered is out of bounds.")    #Assume that we don't need to loop back, but you could try add a .sleep and continue to do so

        elif userInput == "2" or userInput.lower() == "smart tv":
            finalDevices.append(SmartTV())
            print("'Smart TV' device added!")
        
        else:
            print("Invalid Option.")
    
    return finalDevices

def main():
    mySmartHome = SmartHome()
    devicesInSmartHome = setUpHome()    # list of devices
    for device in devicesInSmartHome:
        mySmartHome.addDevice(device)

    mySmartHomeSystem = SmartHomeSystem(mySmartHome)
    mySmartHomeSystem.runWindow()

    


# TEST RUN
main()