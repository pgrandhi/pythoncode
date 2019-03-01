from tkinter import *

class TrafficLights:
    def __init__(self):
        
        window = Tk()
        window.title("Traffic Lights")
        
        self.canvas = Canvas(window, width = 80, height = 180, bg = "white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        
        self.colorVar = IntVar()
        Radiobutton(frame, text="Red", padx = 20,
                    variable=self.colorVar, value=1, command=self.colorChange).grid(row=1, column = 1)
        Radiobutton(frame, text="Yellow", padx = 20,
                    variable=self.colorVar, value=2,command=self.colorChange).grid(row=1, column = 2)
        Radiobutton(frame, text="Green", padx = 20,
                    variable=self.colorVar, value=3, command=self.colorChange).grid(row=1, column = 3)

        self.rectangle = self.create_rectangle(20,20,40,140)
        self.red = self.create_circle(40, 40, 20)
        self.yellow = self.create_circle(40, 90, 20)
        self.green = self.create_circle(40, 140, 20)
        
        window.mainloop()

    def colorChange(self):
        color = self.colorVar.get()
        if color==1:
           self.canvas.itemconfig(self.red,fill="red")
           self.canvas.itemconfig(self.yellow,fill="white")
           self.canvas.itemconfig(self.green,fill="white")
        elif color == 2:
           self.canvas.itemconfig(self.red,fill="white")
           self.canvas.itemconfig(self.yellow,fill="yellow")
           self.canvas.itemconfig(self.green,fill="white")
        elif color == 3:
           self.canvas.itemconfig(self.red,fill="white")
           self.canvas.itemconfig(self.yellow,fill="white")
           self.canvas.itemconfig(self.green,fill="green")
        else:
           self.canvas.itemconfig(self.red,fill="white")
           self.canvas.itemconfig(self.yellow,fill="white")
           self.canvas.itemconfig(self.green,fill="white")
        
    def create_circle(self, x, y, r): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self.canvas.create_oval(x0, y0, x1, y1,fill="white")

    def create_rectangle(self,x, y, width, height):
        x0 = x
        y0 = y
        x1 = x + width
        y1 = y + height
        return self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")


TrafficLights()
