import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from TubeSystem import TubeSystem
from Setting import Setting

class TubeMap():
    def __init__(self):  
        """Settings"""
        self.settings = Setting()
        self.tubeSystem = TubeSystem()

        self.angle = np.radians(self.settings.angle)

        self.tubeGraph = nx.Graph()

    """Functions"""
    # Edge generator functions
    def createEdges(self,lineStaions):
        edges = []
        for i in range(len(lineStaions) - 1):
            edges.append((lineStaions[i],lineStaions[i+1]))
        return edges
    
    def generateEdgeColor(self,edges,color = "blue"):
        edge_colors = []
        for edge in edges:
            if edge in edges:
                edge_colors.append(color)
        
        return edge_colors
    
    def generateEdgeLabel(self,edges,distanceList):
        labels = {}
        for i, edge in enumerate(edges):
            labels[edge] = distanceList[i]

        return labels


    # Position generator functions
    def generatePosition(self,direction_list,start_pos= (0,0)):
        pos = []
        x, y = start_pos
        for direction in direction_list:
            dx, dy = self.getOffsetAndAlignment(direction,"direction")
            x += dx
            y += dy
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
        for line in self.tubeSystem.lines:
            plt.plot([], [], color=line["color"], linewidth=2, label=line["key"])

    def generateNodeColorList(self,lineStations,lineColor,interchange):
        node_color_list = []
        node_border_colors = []
        for i in range(len(lineStations)):
            if interchange[i]:
                node_color_list.append(self.settings.interchange_station_color)
                node_border_colors.append(self.settings.interchange_node_color)
            else:
                node_color_list.append(lineColor)
                node_border_colors.append(lineColor)

        return (node_color_list, node_border_colors)
    
    # Label
    def labelStationNames(self,lineStations, linePos,placementList):
        for i,station in enumerate(lineStations):
            (x,y) = linePos[station]
            placement= placementList[i]
            self.setLabelOffset(station,x,y,placement)
            
    def setLabelOffset(self,station,x,y,placement):
        dx, dy, ha, va = self.getOffsetAndAlignment(placement)
        x += dx * self.settings.label_x_offset
        y += dy * self.settings.label_y_offset
        self.pltTextStationName(x,y,station,ha,va)

    # Others
    def pltTextStationName(self,x,y,station,ha,va):
        plt.text(x, y, station, ha= ha, va= va,fontsize = self.settings.fontSize)

    def getOffsetAndAlignment(self,key,mode="placement"):
        if mode == "placement":
            offsets = {
                "t":   (0, 1, 'center', 'bottom'),
                "tr":  (1, 1, 'left', 'bottom'),
                "r":   (1, 0, 'left', 'center'),
                "br":  (1, -1, 'left', 'bottom'),
                "b":   (0, -1, 'center', 'top'),
                "bl":  (-1, -1, 'right', 'bottom'),
                "l":   (-1, 0, 'right', 'center'),
                "tl":  (-1, 1, 'right', 'bottom')
            }
            dx, dy, ha, va = offsets.get(key, (0, 0, 'center', 'center'))
            return (dx, dy, ha, va)
        
        else: # For direction
            distance = self.settings.distance
            directions = {
                "N":  (0, 1),
                "NE": (np.cos(self.angle), np.sin(self.angle)),
                "E":  (1, 0),
                "SE": (np.cos(self.angle), -np.sin(self.angle)),
                "S":  (0, -1),
                "SW": (-np.cos(self.angle), -np.sin(self.angle)),
                "W":  (-1, 0),
                "NW": (-np.cos(self.angle), np.sin(self.angle))
            }
            dx, dy = directions.get(key,(0,0))
            return (dx * distance, dy * distance)

    """Graph"""

    def createLine(self,linedata):
        station = linedata["station"]
        color = linedata["color"]
        direction = linedata["direction"]
        distance = linedata["distance"]
        interchange = linedata["interchange"]
        namePlacement = linedata["placement"]

        pos = self.generateStationPosition(station,direction)
        edges = self.createEdges(station)
        self.tubeGraph.add_edges_from(edges)
        nodeColor, nodeBorder = self.generateNodeColorList(station,color,interchange)
        labels = self.generateEdgeLabel(edges,distance)
        edge_color = self.generateEdgeColor(edges,color)
        
        self.labelStationNames(station,pos,namePlacement)
        
      
        return (pos,nodeColor, nodeBorder,labels,edge_color)
    

    def drawTubeMap(self,figsize = (10,7)):
        plt.figure(figsize=figsize)  
        pos, nodeColor, nodeBorder,labels, edge_colors = self.createLine(self.tubeSystem.piccadilly)
        
        nx.draw(self.tubeGraph, 
                pos, 
                node_color= nodeColor,
                edgecolors = nodeBorder,
                edge_color = edge_colors)
        
        nx.draw_networkx_edge_labels(self.tubeGraph,pos,edge_labels=labels)

        
        self.generateLineColorLegend()
        plt.title(self.settings.digram_name)
        plt.legend(title = self.settings.legend_title,loc = self.settings.legend_location)
        plt.show()


try:
    if __name__ == '__main__':
        tubeMap = TubeMap()
        tubeMap.drawTubeMap()

except Exception as error:
    print(f"Error: {error}")
