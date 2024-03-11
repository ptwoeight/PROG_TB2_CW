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
        screenSizeDiff = 260 + (updatedDeviceCount * 75)   # gap per line
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
        editDeviceWin.geometry("185x85")
        editDeviceFrame = Frame(editDeviceWin)
        editDeviceFrame.grid(padx=15, pady=15)
        deviceType = type(self.smartHome.getDeviceAt(index))
        
        if deviceType == SmartTV:
            setChannel = StringVar()
            setChannel.set(self.devices[index].getChannel())
            setChannelAsInt = setChannel.get()

            lblUpdateChannel = Label(
                editDeviceFrame,
                text="Set new Smart TV channel:"
            )
            lblUpdateChannel.grid(column=0, row=0, columnspan=2)

            ntrUpdateChannel = Entry(
                editDeviceFrame,
                textvariable=setChannel,
                width=12
            )
            ntrUpdateChannel.grid(column=0, row=1, sticky=E)

            btnEnterUpdate = Button(
                editDeviceFrame,
                text="Set",
                width=4,
                command= lambda: self.setNewChannel(index, setChannel, editDeviceWin, editDeviceFrame)
            )
            btnEnterUpdate.grid(column=1, row=1, sticky=W)

        elif deviceType == SmartPlug:
            setConsumptionRate = StringVar()
            setConsumptionRate.set(self.devices[index].getConsumptionRate())
            setConsumptionRateAsInt = setConsumptionRate.get()

            lblUpdateConsumptionRate = Label(
                editDeviceFrame,
                text="Set new consumption rate:"
            )
            lblUpdateConsumptionRate.grid(column=0, row=0, columnspan=2)

            ntrUpdateConsumptionRate = Entry(
                editDeviceFrame,
                textvariable=setConsumptionRate,
                width=12
            )
            ntrUpdateConsumptionRate.grid(column=0, row=1, sticky=E)

            btnEnterUpdate = Button(
                editDeviceFrame,
                text="Update",
                command= lambda: self.setNewConsumptionRate(index, setConsumptionRate, editDeviceWin, editDeviceFrame)
            )
            btnEnterUpdate.grid(column=1, row=1, sticky=W)

        editDeviceWin.protocol("WM_DELETE_WINDOW", editDeviceWin.destroy)
        editDeviceWin.mainloop()

    def setNewChannel(self, index, newChannel, editDeviceWin, editDeviceFrame): 
        try:
            newChannelAsInt = int(newChannel.get())
            if newChannelAsInt >=1 and newChannelAsInt <= 734:
                self.devices[index].setChannel(newChannelAsInt)
                self.updateWindow()
                editDeviceWin.destroy()
            else:
                editDeviceWin.geometry("185x110")
                lblErrorMessage = Label(
                    editDeviceFrame,
                    text="ERROR: Out of bounds\nValues between 1-734 only",
                    fg="red"
                )
                lblErrorMessage.grid(column=0, row=2, columnspan=2)
        except ValueError:
            editDeviceWin.geometry("185x110")
            lblErrorMessage = Label(
                editDeviceFrame,
                text="ERROR: Not an integer\nValues between 1-734 only",
                fg="red"
            )
            lblErrorMessage.grid(column=0, row=2, columnspan=2)
        
    def setNewConsumptionRate(self, index, newConsumptionRate, editDeviceWin, editDeviceFrame): 
        try:
            newConsumptionRateAsInt = int(newConsumptionRate.get())
            if newConsumptionRateAsInt >= 0 and newConsumptionRateAsInt <= 150:
                self.devices[index].setConsumptionRate(newConsumptionRateAsInt)
                self.updateWindow()
                editDeviceWin.destroy()
            else:
                editDeviceWin.geometry("185x110")
                lblErrorMessage = Label(
                    editDeviceFrame,
                    text="ERROR: Out of bounds\nValues between 0-150 only",
                    fg="red"
                )
                lblErrorMessage.grid(column=0, row=2, columnspan=2)
        except ValueError:
            editDeviceWin.geometry("185x110")
            lblErrorMessage = Label(
                editDeviceFrame,
                text="ERROR: Not an integer\nValues between 0-150 only",
                fg="red"
            )
            lblErrorMessage.grid(column=0, row=2, columnspan=2)


    def addButton(self, win, btnAddDevice): 
        newDeviceWin = Toplevel(win)
        newDeviceWin.title("Add New Device")
        newDeviceWin.geometry("195x80")
        newDeviceFrame = Frame(newDeviceWin)
        newDeviceFrame.grid(padx=15, pady=15)

        lblDevicePrompt = Label(
            newDeviceFrame,
            text="Choose a new device to add:"
        )
        lblDevicePrompt.grid(column=0, row=0, columnspan=2)

        btnSmartPlugOption = Button(
            newDeviceFrame,
            text="Smart Plug",
            command= lambda: self.addSmartPlug(newDeviceWin, newDeviceFrame, btnAddDevice) 
        )
        btnSmartPlugOption.grid(column=0, row=1, sticky=E)

        btnSmartTVOption = Button(
            newDeviceFrame,
            text="Smart TV",
            command= lambda: self.saveNewSmartTV(newDeviceWin, btnAddDevice)
        )
        btnSmartTVOption.grid(column=1, row=1, sticky=W)

        newDeviceWin.mainloop()
   
    def addSmartPlug(self, newDeviceWin, newDeviceFrame, btnAddDevice): 
        newDeviceWin.geometry("195x130")
        consumptionRate = StringVar()

        lblNewPlugPrompt = Label(
            newDeviceFrame,
            text="Set Consumption Rate:"
        )
        lblNewPlugPrompt.grid(column=0, row=2, columnspan=2)

        ntrConsumptionRate = Entry(
            newDeviceFrame,
            width=10,
            textvariable=consumptionRate
        )
        ntrConsumptionRate.grid(column=0, row=3)

        btnEnter = Button(
            newDeviceFrame,
            text="Enter", 
            width=6,
            command= lambda: self.saveNewPlug(newDeviceWin, newDeviceFrame, consumptionRate, btnAddDevice)
        )
        btnEnter.grid(column=1, row=3)

    def saveNewPlug(self, newDeviceWin, newDeviceFrame, consumptionRate, btnAddDevice):
        try:
            consumptionRateAsInt = int(consumptionRate.get())
            if consumptionRateAsInt >= 0 and consumptionRateAsInt <= 150:
                newPlug = SmartPlug(consumptionRateAsInt)  
                self.smartHome.addDevice(newPlug)
                btnAddDevice.grid_forget()
                self.updateWindow()
                newDeviceWin.destroy()
            else:
                newDeviceWin.geometry("195x165")

                lblErrorMessage = Label(
                    newDeviceFrame,
                    text="ERROR: Out of bounds\nValues between 0-150 only",
                    fg="red"
                )
                lblErrorMessage.grid(column=0, row=4, columnspan=2)
        except ValueError:
            newDeviceWin.geometry("195x165")
            
            lblErrorMessage = Label(
                newDeviceFrame,
                text="ERROR: Not an integer\nValues between 0-150 only",
                fg="red"
            )
            lblErrorMessage.grid(column=0, row=4, columnspan=2)

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
                inputConsumptionRate = input("Enter Consumption Rate: ")   

                while not inputConsumptionRate.isdigit():
                    print("Value entered is not an integer.")
                    inputConsumptionRate = input("Enter Consumption Rate: ")

                consumptionRateAsInt = int(inputConsumptionRate)

                if consumptionRateAsInt <= 150 and consumptionRateAsInt >= 0:
                    finalDevices.append(SmartPlug(consumptionRateAsInt))    
                    print("'Smart Plug' device added!")

                    invalidConsumptionRate = False
                else:
                    print("Value entered is out of bounds.")    

        elif userInput == "2" or userInput.lower() == "smart tv":
            finalDevices.append(SmartTV())
            print("'Smart TV' device added!")
        
        else:
            print("Invalid Option.")
    
    return finalDevices

def main():
    mySmartHome = SmartHome()
    devicesInSmartHome = setUpHome()    
    for device in devicesInSmartHome:
        mySmartHome.addDevice(device)

    mySmartHomeSystem = SmartHomeSystem(mySmartHome)
    mySmartHomeSystem.runWindow()

    


# TEST RUN
main()