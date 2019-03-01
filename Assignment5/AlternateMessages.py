from tkinter import *

class AlternateMessages:
    def __init__(self):
        
        window = Tk()
        window.title("Traffic Lights")

        self.message1 ="Programming is fun"
        self.message2 ="It is fun to program"
        self.currentMessage =  self.message1        
        self.canvas = Canvas(window, width = 300, height = 150, bg = "white")        
        self.canvas.create_text(140,40, fill="blue",font="Times 20 italic bold", text=self.message1)        
        self.canvas.bind("<Button-1>",self.onClick)
        self.canvas.pack(expand= YES, fill = BOTH)
              
        window.mainloop()

    def onClick(self,event):
        self.canvas.delete('all')
        if self.currentMessage == self.message1:
            self.currentMessage = self.message2
        else:
            self.currentMessage = self.message2
        self.canvas.create_text(140,40, fill="red",font="Times 20 italic bold", text=self.currentMessage)
                         
   
AlternateMessages()
