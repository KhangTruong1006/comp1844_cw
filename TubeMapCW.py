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
        self.namePosition = TubeSystem.StationNamePosition()

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
    
    def generateEdgeLabel(self,lineStations,distanceList):
        edges = self.createEdges(lineStations)
        labels = {}
        for i, edge in enumerate(edges):
            labels[edge] = distanceList[i]

        return labels

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
    def labelStationNames(self,lineStations, linePos,placementList):
        for i,station in enumerate(lineStations):
            (x,y) = linePos[station]
            placement= placementList[i]
            self.setLabelOffset(station,x,y,placement)
            
    def setLabelOffset(self,station,x,y,placement):
        if placement == "t":
            x,y = x, y + self.settings.label_y_offset
            plt.text(x, y, station, ha= 'center', va='bottom',fontsize = self.settings.fontSize)
        
        elif placement == "tr":
            x,y = x + self.settings.label_x_offset, y + self.settings.label_y_offset
            plt.text(x, y, station, ha= 'left', va='bottom',fontsize = self.settings.fontSize)

        elif placement == "r":
            x,y = x + self.settings.label_x_offset, y 
            plt.text(x, y, station, ha= 'left', va='center',fontsize = self.settings.fontSize)
        
        elif placement == "br":
            x,y = x + self.settings.label_x_offset, y - self.settings.label_y_offset
            plt.text(x, y, station, ha= 'left', va='bottom',fontsize = self.settings.fontSize)

        elif placement == "b":
            x,y = x , y -self.settings.label_y_offset
            plt.text(x, y, station, ha= 'center', va='top',fontsize = self.settings.fontSize)

        elif placement == "bl":
            x,y = x - self.settings.label_x_offset, y - self.settings.label_y_offset
            plt.text(x, y, station, ha= 'right', va='bottom',fontsize = self.settings.fontSize)

        elif placement == "l":
            x,y = x - self.settings.label_x_offset, y
            plt.text(x, y, station, ha= 'right', va='center',fontsize = self.settings.fontSize)

        elif placement == "tl":
            x,y = x - self.settings.label_x_offset, y + self.settings.label_y_offset
            plt.text(x, y, station, ha= 'right', va='bottom',fontsize = self.settings.fontSize)

    """Graph"""
    def createLine(self,lineStations,lineDirection,lineColor,namePlacementList,distanceList):
        line_edges = self.createEdges(lineStations)
        self.tubeGraph.add_edges_from(line_edges)
        pos = self.generateStationPosition(lineStations,lineDirection)
        stationColorList = self.generateNodeColorList(lineStations,lineColor)
        self.labelStationNames(lineStations,pos,namePlacementList)
        labels = self.generateEdgeLabel(lineStations,distanceList)
        return (pos,stationColorList,labels)
    

    def drawTubeMap(self,figsize = (10,7)):
        plt.figure(figsize=figsize)  
        pos, nodeColorList,labels = self.createLine(self.lineStations.piccadilly,
                                             self.direction.piccailly,
                                             self.lineColor.piccadilly,
                                             self.namePosition.piccadilly,
                                             self.stationDistance.piccadilly)
        
        edge_colors = self.generateEdgeColor(self.lineStations.piccadilly)
        
        nx.draw(self.tubeGraph, 
                pos, 
                node_color= nodeColorList,
                edge_color = edge_colors)
        
        nx.draw_networkx_edge_labels(self.tubeGraph,pos,edge_labels=labels)

        
        self.generateLineColorLegend()
        plt.title(self.settings.digram_name)
        plt.legend(title = self.settings.legend_title,loc = "lower right")
        plt.show()


try:
    if __name__ == '__main__':
        tubeMap = TubeMap()
        tubeMap.drawTubeMap()

except Exception as error:
    print(f"Error: {error}")
