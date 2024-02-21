from backend import SmartPlug, SmartTV, SmartHome
from tkinter import *

class SmartHomeSystem:
    def __init__(self, listOfDevices):
        self.win = Tk()
        self.win.title("Smart Home System")
        self.win.geometry("600x350")
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(padx=10, pady=10)
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
            borderwidth=5
        )
        btnTurnOnAll.grid(column=0, row=0)
        
        lblFirstDevice = Label(
            self.mainFrame,
            text=f"{self.devices[0].__class__.__name__}: {self.devices[0].__str__()}"
        )
        lblFirstDevice.grid(column=0, row=1)

        btnAddDevice = Button(
            self.mainFrame,
            text="Add",
            width=15,
            borderwidth=5
        )
        btnAddDevice.grid(column=0, row=7)

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
main()