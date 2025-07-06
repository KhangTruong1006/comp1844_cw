import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

import TubeSystem
from Setting import Setting

class TubeMap():
    def __init__(self):  
        """Settings"""
        self.settings = Setting()

        self.lineStations = TubeSystem.LineStation()
        self.direction = TubeSystem.Direction()
        self.lineColor = TubeSystem.LineColor()
        self.stationDistance = TubeSystem.StationDistance()

        self.angle = np.radians(self.settings.angle)
        self.distance = self.settings.distance

        self.tubeGraph = nx.Graph()

    """Functions"""
    # Edge generator functions
    def createEdges(self,lineStaions):
        edges = []
        for i in range(len(lineStaions) - 1):
            edges.append((lineStaions[i],lineStaions[i+1]))
        return edges
    
    def generateEdgeColor(self,lineStation):
        edges = self.createEdges(lineStation)
        edge_colors = []
        for edge in self.tubeGraph.edges():
            if edge in edges:
                edge_colors.append("blue")

            else:
                edge_colors.append("gray")
        return edge_colors

    # Position generator functions
    def generatePosition(self,direction_list,start_pos= (0,0)):
        pos = []
        for direction in direction_list:
            if direction == "Start":
                x,y = start_pos

            elif direction == "N":
                x,y = x, y+ self.distance

            elif direction == "NE":
                x,y = x + self.distance * np.cos(self.angle) , y + self.distance*np.sin(self.angle)

            elif direction == "E":
                x,y = x + self.distance, y

            elif direction == "SE":
                x,y = x + self.distance * np.cos(self.angle) , y - self.distance*np.sin(self.angle)

            elif direction == "S":
                x,y = x, y - self.distance

            elif direction == "SW":
                x,y = x - self.distance * np.cos(self.angle) , y - self.distance*np.sin(self.angle)

            elif direction == "W":
                x,y = x - self.distance, y 

            elif direction == "NW":
                x,y = x + self.distance * np.cos(self.angle) , y + self.distance*np.sin(self.angle)
            
            pos.append((x,y))

        return pos
            
    def generateStationPosition(self,lineStations,station_direction):
        pos ={}
        stationPos = self.generatePosition(station_direction)
        for i in range(len(lineStations)):
            pos[f'{lineStations[i]}'] = stationPos[i]

        return pos
    
    # Color generator functions
    def generateLineColorLegend(self):
        for line in self.lineColor.list:
            plt.plot([], [], color=line[0], linewidth=2, label=line[1])

    def generateNodeColorList(self,lineStations,lineColor):
        node_color_list = []
        for i in range(len(lineStations)):
            node_color_list.append(lineColor[0])
        return node_color_list
    
    # Others
    def labelStationNames(self,lineStations, linePos):
        for station in lineStations:
            (x,y) = linePos[station]
            plt.text(x - 1, y + 0.2 , station, ha= 'center', va='bottom',fontsize = self.settings.fontSize)
    
    """Graph"""
    def createLine(self,lineStations,lineDirection,lineColor):
        line_edges = self.createEdges(lineStations)
        self.tubeGraph.add_edges_from(line_edges)
        pos = self.generateStationPosition(lineStations,lineDirection)
        stationColorList = self.generateNodeColorList(lineStations,lineColor)
        self.labelStationNames(lineStations,pos)

        return (pos,stationColorList)
    

    def drawTubeMap(self):  
        pos, nodeColorList = self.createLine(self.lineStations.piccadilly,self.direction.piccailly,self.lineColor.piccadilly)
        edge_colors = self.generateEdgeColor(self.lineStations.piccadilly)
        nx.draw(self.tubeGraph, 
                pos, 
                node_color= nodeColorList,
                edge_color = edge_colors)

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
