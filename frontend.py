from backend import SmartPlug, SmartTV, SmartHome
from tkinter import *

class SmartHomeSystem:
    def __init__(self, listOfDevices):
        self.win = Tk()
        self.win.title("Smart Home System")
        self.win.geometry("675x275")
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
            width=30,
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
            width=25,
            borderwidth=5
        )
        btnAddDevice.grid(column=0, row=6, sticky=W)

        #column 1
        btnToggle1 = Button(
            self.mainFrame,
            text="Toggle",
            width=15,
            borderwidth=5
       )
        btnToggle1.grid(column=1, row=1, sticky=W)

        btnToggle2 = Button(
            self.mainFrame,
            text="Toggle",
            width=15,
            borderwidth=5
        )
        btnToggle2.grid(column=1, row=2, sticky=W)

        btnToggle3 = Button(
            self.mainFrame,
            text="Toggle",
            width=15,
            borderwidth=5
        )
        btnToggle3.grid(column=1, row=3, sticky=W)

        btnToggle4 = Button(
            self.mainFrame,
            text="Toggle",
            width=15,
            borderwidth=5
        )
        btnToggle4.grid(column=1, row=4, sticky=W)

        btnToggle5 = Button(
            self.mainFrame,
            text="Toggle",
            width=15,
            borderwidth=5
        )
        btnToggle5.grid(column=1, row=5, sticky=W)

        btnTurnOffAll = Button(
            self.mainFrame,
            text="Turn off all",
            width=30,
            borderwidth=5
        )
        btnTurnOffAll.grid(column=1, row=0, columnspan=2, sticky=W)

        #column 2
        btnEdit1 = Button(
            self.mainFrame,
            text="Edit",
            width=10,
            borderwidth=5
        )
        btnEdit1.grid(column=2, row=1, sticky=W)

        btnEdit2 = Button(
            self.mainFrame,
            text="Edit",
            width=10,
            borderwidth=5
        )
        btnEdit2.grid(column=2, row=2, sticky=W)

        btnEdit3 = Button(
            self.mainFrame,
            text="Edit",
            width=10,
            borderwidth=5
        )
        btnEdit3.grid(column=2, row=3, sticky=W)

        btnEdit4 = Button(
            self.mainFrame,
            text="Edit",
            width=10,
            borderwidth=5
        )
        btnEdit4.grid(column=2, row=4, sticky=W)

        btnEdit5 = Button(
            self.mainFrame,
            text="Edit",
            width=10,
            borderwidth=5
        )
        btnEdit5.grid(column=2, row=5, sticky=W)

        #column 3
        btnDelete1 = Button(
            self.mainFrame,
            text="Delete",
            width=15,
            borderwidth=5
        )
        btnDelete1.grid(column=3, row=1, sticky=W)
        
        btnDelete2 = Button(
            self.mainFrame,
            text="Delete",
            width=15,
            borderwidth=5
        )
        btnDelete2.grid(column=3, row=2, sticky=W)
        
        btnDelete3 = Button(
            self.mainFrame,
            text="Delete",
            width=15,
            borderwidth=5
        )
        btnDelete3.grid(column=3, row=3, sticky=W)

        btnDelete4 = Button(
            self.mainFrame,
            text="Delete",
            width=15,
            borderwidth=5
        )
        btnDelete4.grid(column=3, row=4, sticky=W)

        btnDelete5 = Button(
            self.mainFrame,
            text="Delete",
            width=15,
            borderwidth=5
        )
        btnDelete5.grid(column=3, row=5, sticky=W)

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

def main():
    devicesInSmartHome = setUpHome()    # list of devices

    mySmartHomeSystem = SmartHomeSystem(devicesInSmartHome)
    mySmartHomeSystem.runWindow()

    


# TEST RUN
main()