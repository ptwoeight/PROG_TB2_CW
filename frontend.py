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
        self.listOfWidgets = []

    def runWindow(self):
        self.updateDeviceDetails()
        self.createWidgets()
        
        self.win.mainloop()

    def resizeWindow(self):
        updatedDeviceCount = self.deviceCount - 5 # default is 5
        screenSizeDiff = 260 + (updatedDeviceCount * 30)   # gap per line
        self.win.geometry(f"620x{screenSizeDiff}")

    def updateWindow(self):
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


    def createWidgets(self):
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
                command= lambda index=i: self.editButton(index)
            )
            btnEdit.grid(column=2, row=i+1, sticky=W)
            self.listOfWidgets.append(btnEdit)

        for i in range(self.deviceCount):
            btnDelete = Button(
                self.mainFrame,
                text="Delete",
                width=15,
                borderwidth=5,
                command= lambda index=i: self.deleteButton(index)
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
        self.listOfWidgets.append(btnAddDevice)

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

    def deleteButton(self, index):
        self.smartHome.removeDeviceAt(index)
        for widget in self.listOfWidgets:
            widget.grid_forget()
        self.updateWindow()


    def editButton(self, index):
        editDeviceWin = Toplevel(self.win)
        editDeviceWin.title("Edit Device")
        editDeviceWin.geometry("175x85")
        editDeviceFrame = Frame(editDeviceWin)
        editDeviceFrame.grid(padx=15, pady=15)
        deviceType = type(self.smartHome.getDeviceAt(index))
        
        if deviceType == SmartTV:
            setChannel = IntVar()
            setChannel.set(self.devices[index].getChannel())
            setChannelAsInt = setChannel.get()

            lblUpdateChannel = Label(
                editDeviceFrame,
                text="Update Smart TV channel:"
            )
            lblUpdateChannel.grid(column=0, row=0)

            ntrUpdateChannel = Entry(
                editDeviceFrame,
                textvariable=setChannel,
                width=12
            )
            # note for potential code
            ntrUpdateChannel.grid(column=0, row=1, sticky=W)

            btnEnterUpdate = Button(
                editDeviceFrame,
                text="Set",
                width=4,
                command= lambda: self.setNewChannel(index, setChannel, editDeviceWin)
            )
            btnEnterUpdate.grid(column=0, row=1, sticky=E)

        elif deviceType == SmartPlug:
            setConsumptionRate = IntVar()
            setConsumptionRate.set(self.devices[index].getConsumptionRate())
            setConsumptionRateAsInt = setConsumptionRate.get()

            lblUpdateConsumptionRate = Label(
                editDeviceFrame,
                text="Update consumption rate:"
            )
            lblUpdateConsumptionRate.grid(column=0, row=0, columnspan=2)

            ntrUpdateConsumptionRate = Entry(
                editDeviceFrame,
                textvariable=setConsumptionRate,
                width=12
            )
            ntrUpdateConsumptionRate.grid(column=0, row=1, sticky=W)

            btnEnterUpdate = Button(
                editDeviceFrame,
                text="Update",
                command= lambda: self.setNewConsumptionRate(index, setConsumptionRate, editDeviceWin)
            )
            btnEnterUpdate.grid(column=1, row=1, sticky=E)

        editDeviceWin.protocol("WM_DELETE_WINDOW", editDeviceWin.destroy)
        editDeviceWin.mainloop()

    def setNewChannel(self, index, newChannel, editDeviceWin): # 1-734, if out of range, exit window - device stays the same
        # add error handling for if not int and if 1-734 (inclusive)
        newChannelAsInt = newChannel.get()
        self.devices[index].setChannel(newChannelAsInt)
        self.updateWindow()
        editDeviceWin.destroy()

    def setNewConsumptionRate(self, index, newConsumptionRate, editDeviceWin): #0-150, if out of range, exit window - device stays the same
        # add error handling for if not in and if 150
        # error handling: display message, set it to what it was previously
        newConsumptionRateAsInt = newConsumptionRate.get()
        self.devices[index].setConsumptionRate(newConsumptionRateAsInt)
        self.updateWindow()
        editDeviceWin.destroy()


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
            command= lambda: self.addSmartPlug(newDeviceWin, newDeviceFrame, btnAddDevice) 
        )
        btnSmartPlugOption.grid(column=0, row=1, sticky=W)

        btnSmartTVOption = Button(
            newDeviceFrame,
            text="Smart TV",
            command= lambda: self.saveNewSmartTV(newDeviceWin, btnAddDevice)
        )
        btnSmartTVOption.grid(column=1, row=1, sticky=E)

        newDeviceWin.mainloop()
   
    def addSmartPlug(self, newDeviceWin, newDeviceFrame, btnAddDevice): # if out of range, exit window - no devices added
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
        newPlug = SmartPlug(consumptionRate.get())  
        self.smartHome.addDevice(newPlug)
        btnAddDevice.grid_forget()
        self.updateWindow()
        newDeviceWin.destroy()


    def saveNewSmartTV(self, newDeviceWin, btnAddDevice):
        newSmartTV = SmartTV()  
        self.smartHome.addDevice(newSmartTV)
        btnAddDevice.grid_forget()
        self.updateWindow()
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