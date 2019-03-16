from tkinter import *
import turtle
from collections import namedtuple

vertex = namedtuple("vertexId","vertexId x y")            
edge = namedtuple("vertexId","vertexId edge")
class printGraph:
    def __init__(self):
        window = Tk()
        window.title("Graph")
        self.canvas = Canvas(window, width= 200, height = 200, bg="white")
        self.canvas.pack()
        
        self.filename = input("Enter a filename:")
        self.graph = []
        self.vertexList = []
        self.vertexEdges = []
        self.numVertices = self.readFromFile()
        self.printEdges()
        
    def readFromFile(self):
        infile = open(self.filename,"r")    
        line = infile.readline()
        numVertices = int(line)
        while line:
            line = infile.readline()
            self.graph.append(line)       
        infile.close()
        return numVertices

    def printEdges(self):        
        for item in self.graph:            
            vertexInfo = item.split()
            if len(vertexInfo)>0:
               vertexX = vertex(int(vertexInfo[0]), int(vertexInfo[1]),int(vertexInfo[2]))
               self.vertexList.append(vertexX)
               for i in range(3, len(vertexInfo)):
                   vertexEdge = edge(int(vertexInfo[0]),int(vertexInfo[i]))                   
                   self.vertexEdges.append(vertexEdge)        
        self.drawEdges()
            
    def drawEdges(self):        
        for item in self.vertexEdges:
            startVertex = item.vertexId
            endVertex = item.edge
            startX = self.vertexList[startVertex].x
            startY = self.vertexList[startVertex].y
            endX =  self.vertexList[endVertex].x
            endY =  self.vertexList[endVertex].y
            self.canvas.create_text(startX-5, startY-5, fill = 'black', text='{}'.format(startVertex))
            self.canvas.create_oval(startX, startY, startX, startY, width = 2, fill = 'black')
            self.canvas.create_line(startX, startY, endX, endY)
        
printGraph()
