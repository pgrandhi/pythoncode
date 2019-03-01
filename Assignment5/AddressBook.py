from tkinter import *

class AddressBook:
    def __init__(self):
        window = Tk()
        window.title("AddressBook")

        nameFrame = Frame(window)
        Label(nameFrame, text="Name").grid(row=0,column=0, sticky=W)
        self.nameVar = StringVar()
        Entry(nameFrame,textvariable=self.nameVar, width = 50, justify=LEFT).grid(row=0,column=1)
        nameFrame.grid(row=1,sticky=W)

        streetFrame = Frame(window)
        Label(streetFrame, text="Street").grid(row=0,column=0, sticky=W)
        self.streetVar = StringVar()
        Entry(streetFrame,textvariable=self.streetVar, width = 50,justify=LEFT).grid(row=0,column=1)
        streetFrame.grid(row=2,sticky=W)

        thirdFrame = Frame(window)
        cityFrame = Frame(thirdFrame)
        Label(cityFrame, text="City").grid(row=0,column=0,sticky=W)
        self.cityVar = StringVar()
        Entry(cityFrame,textvariable=self.cityVar,width = 25, justify=LEFT).grid(row=0,column=1)
        cityFrame.grid(row=0,column=0,sticky=W)

        stateFrame = Frame(thirdFrame)
        Label(stateFrame, text="State").grid(row=0, column=0,sticky=W)
        self.stateVar = StringVar()
        Entry(stateFrame,textvariable=self.stateVar,width = 6, justify=LEFT).grid(row=0,column=1)
        stateFrame.grid(row=0,column=1, sticky=W)
        
        zipFrame = Frame(thirdFrame)
        Label(zipFrame, text="ZIP").grid(row=0, column=0,sticky=W)
        self.zipVar = StringVar()
        Entry(zipFrame,textvariable=self.stateVar,width = 10, justify=LEFT).grid(row=0,column=1)
        zipFrame.grid(row=0, column=2, sticky=W)
        thirdFrame.grid(row=3,sticky=W)

        buttonFrame = Frame(window)   
        Button(buttonFrame,text="Add").grid(row=0,column=0, sticky=W)
        Button(buttonFrame,text="First").grid(row=0,column=1,sticky=W)
        Button(buttonFrame,text="Next").grid(row=0,column=2,sticky=W)
        Button(buttonFrame,text="Previous").grid(row=0,column=3,sticky=W)
        Button(buttonFrame,text="Last").grid(row=0,column=4,sticky=W)
        buttonFrame.grid(row=4)        
        
        window.mainloop()
        
 
AddressBook()
        
