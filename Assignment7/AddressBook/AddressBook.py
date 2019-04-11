from tkinter import *
import pymysql

from ReadConfig import read_db_config
db=None

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
        Entry(zipFrame,textvariable=self.zipVar,width = 10, justify=LEFT).grid(row=0,column=1)
        zipFrame.grid(row=0, column=2, sticky=W)
        thirdFrame.grid(row=3,sticky=W)

        buttonFrame = Frame(window)   
        Button(buttonFrame,command=self.buttonClick,text="Add").grid(row=0,column=0, sticky=W)
        Button(buttonFrame,command=self.buttonFirst,text="First").grid(row=0,column=1,sticky=W)
        Button(buttonFrame,command=self.buttonNext,text="Next").grid(row=0,column=2,sticky=W)
        Button(buttonFrame,command=self.buttonPrevious,text="Previous").grid(row=0,column=3,sticky=W)
        Button(buttonFrame,command=self.buttonLast,text="Last").grid(row=0,column=4,sticky=W)
        buttonFrame.grid(row=4)        
        self.id = 0
        window.mainloop()

    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        try:
            dbParam = read_db_config()
            db = pymysql.connect(**dbParam)
            cursor = db.cursor()

            sql = "INSERT INTO addressbook(Name, Street, City, State, Zip) \
                VALUES ('%s', '%s', '%s', '%s','%s')" % (self.nameVar.get(), self.streetVar.get(),
                                                         self.cityVar.get(), self.stateVar.get(), self.zipVar.get())

            cursor.execute(sql)
            db.commit()
            print("Name added to addressbook successfully.")
            db.close()
        except ValueError:
            print("one of your inputs is invalid")
        except Exception as err:
            print("Error:{0}".format(err))

    def buttonFirst(self):
        """ handle button click event and output text from entry area"""
        try:
            dbParam = read_db_config()
            db = pymysql.connect(**dbParam)
            cursor = db.cursor()
            self.id = 1
            sql = "SELECT * from addressbook where Id= %s"
            cursor.execute(sql,self.id)
            records = cursor.fetchall()
            row = records[0]
            self.nameVar.set(row[1])
            self.streetVar.set(row[2])
            self.cityVar.set(row[3])
            self.stateVar.set(row[4])
            self.zipVar.set(row[5])
            db.close()

        except ValueError:
            print("one of your inputs is invalid")
        except Exception as err:
            print("Error:{0}".format(err))

    def buttonNext(self):
        """ handle button click event and output text from entry area"""
        try:
            dbParam = read_db_config()
            db = pymysql.connect(**dbParam)
            cursor = db.cursor()
            self.id = self.id+1
            sql = "SELECT * from addressbook where Id= %s"
            cursor.execute(sql,self.id)
            records = cursor.fetchall()
            row = records[0]
            self.nameVar.set(row[1])
            self.streetVar.set(row[2])
            self.cityVar.set(row[3])
            self.stateVar.set(row[4])
            self.zipVar.set(row[5])
            db.close()

        except ValueError:
            print("one of your inputs is invalid")
        except Exception as err:
            print("Error:{0}".format(err))

    def buttonPrevious(self):
        """ handle button click event and output text from entry area"""
        try:
            dbParam = read_db_config()
            db = pymysql.connect(**dbParam)
            cursor = db.cursor()
            self.id = self.id-1
            sql = "SELECT * from addressbook where Id= %s"
            cursor.execute(sql,self.id)
            records = cursor.fetchall()
            row = records[0]
            self.nameVar.set(row[1])
            self.streetVar.set(row[2])
            self.cityVar.set(row[3])
            self.stateVar.set(row[4])
            self.zipVar.set(row[5])
            db.close()

        except ValueError:
            print("one of your inputs is invalid")
        except Exception as err:
            print("Error:{0}".format(err))

    def buttonLast(self):
        """ handle button click event and output text from entry area"""
        try:
            dbParam = read_db_config()
            db = pymysql.connect(**dbParam)
            cursor = db.cursor()

            sql = "SELECT * from addressbook"
            cursor.execute(sql)
            records = cursor.fetchall()
            self.id = len(records)- 1
            row = records[self.id]
            self.nameVar.set(row[1])
            self.streetVar.set(row[2])
            self.cityVar.set(row[3])
            self.stateVar.set(row[4])
            self.zipVar.set(row[5])
            db.close()

        except ValueError:
            print("one of your inputs is invalid")
        except Exception as err:
            print("Error:{0}".format(err))

AddressBook()

