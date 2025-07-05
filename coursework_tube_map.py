import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

import TubeSystem

class TubeMap():
    def __init__(self):  
        """Settings"""
        self.lineStations = TubeSystem.LineStation()
        self.direction = TubeSystem.Direction()
        self.lineColor = TubeSystem.LineColor()
        self.stationDistance = TubeSystem.StationDistance()

        self.angle = np.radians(45)
        self.distance = 2

        self.tubeGraph = nx.Graph()

    """Functions"""
    def createEdges(self,lineStaions):
        edges = []
        for i in range(len(lineStaions) - 1):
            edges.append((lineStaions[i],lineStaions[i+1]))
        return edges
    
    def generatePosition(self,direction_list,start_pos= (0,0)):
        pos = []
        for direction in direction_list:
            if direction == "Start":
                x,y = start_pos

            elif direction == "N":
                x,y = x, y+ self.distance

            elif direction == "NE":
                x,y = x + self.distance * np.sin(self.angle) , y + self.distance*np.sin(self.angle)

            elif direction == "E":
                x,y = x + self.distance, y

            elif direction == "SE":
                x,y = x + self.distance * np.sin(self.angle) , y - self.distance*np.sin(self.angle)

            elif direction == "S":
                x,y = x, y - self.distance

            elif direction == "SW":
                x,y = x - self.distance * np.sin(self.angle) , y - self.distance*np.sin(self.angle)

            elif direction == "W":
                x,y = x - self.distance, y 

            elif direction == "NW":
                x,y = x + self.distance - np.sin(self.angle) , y + self.distance*np.sin(self.angle)
            
            pos.append((x,y))

        return pos
            
    def generateStationPosition(self,stations,station_direction):
        pos ={}
        stationPos = self.generatePosition(station_direction)
        for i in range(len(stations)):
            pos[f'{stations[i]}'] = stationPos[i]

        return pos
    
    def generateLineColorLegend(self):
        for line in self.lineColor.list:
            plt.plot([], [], color=line[0], linewidth=2, label=line[1])

    
    """Graph"""
    def drawTubeMap(self):
        
        piccadilly_line_edges = self.createEdges(self.lineStations.piccadilly)
        self.tubeGraph.add_edges_from(piccadilly_line_edges)
        piccadillyPos = self.generateStationPosition(self.lineStations.piccadilly,self.direction.piccailly)
        
        nx.draw(self.tubeGraph, piccadillyPos, node_color= self.lineColor.piccadilly[0])

        self.generateLineColorLegend()
        plt.title('London Tube Map')
        plt.legend(loc = "lower right")
        plt.show()


try:
    if __name__ == '__main__':
        tubeMap = TubeMap()
        tubeMap.drawTubeMap()

except Exception as error:
    print(f"Error: {error}")
