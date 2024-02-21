from backend import SmartPlug, SmartTV, SmartHome
from tkinter import *

class SmartHomeSystem:
    def __init__(self, listOfDevices):
        self.win = Tk()
        self.win.title("Smart Home System")
        self.win.geometry("650x200")
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(padx=15, pady=15)
        self.devices = listOfDevices

    def runWindow(self):
        self.createWidgets()
        self.win.mainloop()
        
    def createWidgets(self):
        #column 0
        btnTurnOnAll = Button(
            self.mainFrame,
            text="Turn on all",
            width=20,
            borderwidth=5,
        )
        btnTurnOnAll.grid(column=0, row=0, sticky=W)
        
        lblFirstDevice = Label(
            self.mainFrame,
            text=f"{self.devices[0].__class__.__name__}: {self.devices[0].__str__()}"
        )
        lblFirstDevice.grid(column=0, row=1, sticky=W)

        lblSecondDevice = Label(
            self.mainFrame,
            text=f"{self.devices[1].__class__.__name__}: {self.devices[1].__str__()}"
        )
        lblSecondDevice.grid(column=0, row=2, sticky=W)

        lblThirdDevice = Label(
            self.mainFrame,
            text=f"{self.devices[2].__class__.__name__}: {self.devices[2].__str__()}"
        )
        lblThirdDevice.grid(column=0, row=3, sticky=W)

        lblFourthDevice = Label(
            self.mainFrame,
            text=f"{self.devices[3].__class__.__name__}: {self.devices[3].__str__()}"
        )
        lblFourthDevice.grid(column=0, row=4, sticky=W)

        lblFifthDevice = Label(
            self.mainFrame,
            text=f"{self.devices[4].__class__.__name__}: {self.devices[4].__str__()}"
        )
        lblFifthDevice.grid(column=0, row=5, sticky=W)

        btnAddDevice = Button(
            self.mainFrame,
            text="Add",
            width=15,
            borderwidth=5
        )
        btnAddDevice.grid(column=0, row=6, sticky=W)

def setUpHome():
    mySmartHome = SmartHome()
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

def createSmartHomeSystem():
    devicesInSmartHome = setUpHome()    # list of devices

    mySmartHomeSystem = SmartHomeSystem(devicesInSmartHome)
    mySmartHomeSystem.runWindow()

    


# TEST RUN
createSmartHomeSystem()