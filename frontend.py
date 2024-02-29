from backend import SmartPlug, SmartTV, SmartHome
from tkinter import *

class SmartHomeSystem:
    def __init__(self, smartHome):
        self.smartHome = smartHome
        self.win = Tk()
        self.win.title("Smart Home System")
        self.win.geometry("620x260")
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(padx=15, pady=15)
        self.devices = self.smartHome.getDevices()
        self.deviceCount = len(self.devices)

    def runWindow(self):
        self.updateDeviceDetails()
        self.createWidgets()
        
        self.win.mainloop()

    def resizeWindow(self):
        updatedDeviceCount = self.deviceCount - 5 # default is 5
        screenSizeDiff = 260 + (updatedDeviceCount * 30)   # gap per line
        self.win.geometry(f"620x{screenSizeDiff}")

    def updateWindow(self, btnAddDevice):
        btnAddDevice.grid_forget()
        self.updateDeviceDetails()
        self.createWidgets()
        self.resizeWindow()

    def updateDeviceDetails(self):
        self.devices = self.smartHome.getDevices()
        self.deviceCount = len(self.devices)
        self.formatCurrentDevices()
    
    def formatCurrentDevices(self):
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
        self.updateDeviceDetails()

        btnTurnOnAll = Button(
            self.mainFrame,
            text="Turn on all",
            width=30,
            borderwidth=5,
            command=self.turnOnAllButton
        )
        btnTurnOnAll.grid(column=0, row=0, sticky=W)
        self.listOfWidgets.append(btnTurnOnAll)

        btnTurnOffAll = Button(
            self.mainFrame,
            text="Turn off all",
            width=30,
            borderwidth=5,
            command=self.turnOffAllButton
        )
        btnTurnOffAll.grid(column=1, row=0, columnspan=2, sticky=W)
        self.listOfWidgets.append(btnTurnOffAll)

        for i in range(self.deviceCount):
            btnToggle = Button(
                self.mainFrame,
                text="Toggle",
                width=15,
                borderwidth=5,
                command= lambda index=i: self.toggleButton(index)
            )   
            btnToggle.grid(column=1, row=i+1, sticky=W)
            self.listOfWidgets.append(btnToggle)

        for i in range(self.deviceCount):
            btnEdit = Button(
                self.mainFrame,
                text="Edit",
                width=10,
                borderwidth=5,
                command= lambda: self.editButton(i)
            )
            btnEdit.grid(column=2, row=i+1, sticky=W)
            self.listOfWidgets.append(btnEdit)

        for i in range(self.deviceCount):
            btnDelete = Button(
                self.mainFrame,
                text="Delete",
                width=15,
                borderwidth=5,
                command= lambda: self.deleteButton(i, btnAddDevice, btnToggle, btnEdit, btnDelete)
            )
            btnDelete.grid(column=3, row=i+1, sticky=W)
            self.listOfWidgets.append(btnDelete)

        btnAddDevice = Button(
            self.mainFrame,
            text="Add",
            width=25,
            borderwidth=5,
            command= lambda: self.addButton(self.win, btnAddDevice)
        )
        btnAddDevice.grid(column=0, row=len(self.devices)+1, sticky=W)

    def createLabels(self):
        self.updateDeviceDetails()

        for i in range(self.deviceCount):
            lblDevice = Label(
                self.mainFrame,
                text=self.messages[i]
            )
            lblDevice.grid(column=0, row=i+1, sticky=W)
            self.listOfWidgets.append(lblDevice)
            

    def turnOnAllButton(self):
        self.smartHome.turnOnAll()
        self.formatCurrentDevices()
        self.createLabels()
    
    def turnOffAllButton(self):
        self.smartHome.turnOffAll()
        self.formatCurrentDevices()
        self.createLabels()

    def toggleButton(self, index):
        self.smartHome.toggleSwitch(index)
        self.formatCurrentDevices()
        self.createLabels()
    
    def editButton(self, index): #add button?
        editDeviceWin = Toplevel(self.win)
        editDeviceWin.title("Edit Device")
        editDeviceWin.geometry("80x80")
        editDeviceFrame = Frame(editDeviceWin)
        editDeviceFrame.grid(padx=15, pady=15)
        deviceType = type(self.smartHome.getDeviceAt(index))

        if deviceType == SmartPlug:
            editDeviceWin.geometry("150x80")
            lblUpdateConsumptionRate = Label(
                editDeviceFrame,
                text="Update consumption rate:"
            )
            lblUpdateConsumptionRate.grid(column=0, row=0, columnspan=2, sticky=N)

            ntrUpdateConsumptionRate = Entry(
                editDeviceFrame,
                textvariable=self.devices[index].getConsumptionRate(),
                width=10
            )
            ntrUpdateConsumptionRate.grid(column=0, row=1, columnspan=2, sticky=W)

            btnEnterUpdate = Button(
                editDeviceFrame,
                text="Update"
            )
            btnEnterUpdate.grid(column=1, row=1, sticky=E)

        elif deviceType == SmartTV:
            setChannel = self.devices[index].getChannel()
            editDeviceWin.geometry("150x85")

            lblUpdateChannel = Label(
                editDeviceFrame,
                text="Set Smart TV channel:"
            )
            lblUpdateChannel.grid(column=0, row=0)

            ntrUpdateChannel = Entry(
                editDeviceFrame,
                textvariable=setChannel,
                width=12
            )
            ntrUpdateChannel.insert(0, self.devices[index].getChannel())
            ntrUpdateChannel.grid(column=0, row=1, sticky=W)

            btnEnterUpdate = Button(
                editDeviceFrame,
                text="Set",
                width=4
            )
            btnEnterUpdate.grid(column=0, row=1, sticky=E)
        
        editDeviceWin.mainloop()

        # ~~~~~~~~~~~~~~ YOU'RE HERE! ~~~~~~~~~~~~~~ #

    def deleteButton(self, index, btnAddDevice, btnToggle, btnEdit, btnDelete):
        self.smartHome.removeDeviceAt(index)

        for widget in self.listOfWidgets:
            widget.grid_forget()

        self.updateWindow(btnAddDevice)

        

    def addButton(self, win, btnAddDevice):
        newDeviceWin = Toplevel(win)
        newDeviceWin.title("Add New Device")
        newDeviceWin.geometry("160x80")
        newDeviceFrame = Frame(newDeviceWin)
        newDeviceFrame.grid(padx=15, pady=15)

        lblDevicePrompt = Label(
            newDeviceFrame,
            text="Choose a device to add:"
        )
        lblDevicePrompt.grid(column=0, row=0, sticky=N, columnspan=2)

        btnSmartPlugOption = Button(
            newDeviceFrame,
            text="Smart Plug",
            command= lambda: self.addSmartPlug(newDeviceWin, newDeviceFrame, btnAddDevice) # add command to extend window and call method: entry field for consumption rate 
        )
        btnSmartPlugOption.grid(column=0, row=1, sticky=W)

        btnSmartTVOption = Button(
            newDeviceFrame,
            text="Smart TV"
        )
        btnSmartTVOption.grid(column=1, row=1, sticky=E)

        newDeviceWin.mainloop()
    
    def addSmartPlug(self, newDeviceWin, newDeviceFrame, btnAddDevice):
        newDeviceWin.geometry("160x130")
        consumptionRate = IntVar()

        lblNewPlugPrompt = Label(
            newDeviceFrame,
            text="Set Consumption Rate:"
        )
        lblNewPlugPrompt.grid(column=0, row=2, sticky=N, columnspan=2)

        ntrConsumptionRate = Entry(
            newDeviceFrame,
            width=12,
            textvariable=consumptionRate
        )
        ntrConsumptionRate.grid(column=0, row=3, sticky=W, columnspan=2)

        btnEnter = Button(
            newDeviceFrame,
            text="Enter", # consider making this a check mark
            command= lambda: self.saveNewPlug(newDeviceWin, consumptionRate, btnAddDevice)
        )
        btnEnter.grid(column=1, row=3, sticky=E, columnspan=2)

    def saveNewPlug(self, newDeviceWin, consumptionRate, btnAddDevice):
        newPlug = SmartPlug(consumptionRate.get())  # converts to int..?
        self.smartHome.addDevice(newPlug)
        self.updateWindow(btnAddDevice)
        newDeviceWin.destroy()

        







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