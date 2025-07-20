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
    def generatePositions(self,placeholders,directions,mode = "direction",start_pos = (0,0)):
        dictionary= {}
        x, y = start_pos
        for i, direction in enumerate(directions):
            dx, dy = self.getOffsetAndAlignment(direction,mode)
            x += dx
            y += dy
            dictionary[f'{placeholders[i]}'] = (x,y)

        return dictionary

    def generateStationPos(self,placeholders,directions,start_pos = (0,0)):
        pos = self.generatePositions(placeholders,directions,start_pos=start_pos)
        return pos


    def createNode(self,name,pos,color = "blue"):
        self.tubeGraph.add_node(name,npos = pos, ccn= color)

    def addStationNode(self,line_data,color = "blue"):
        for station in line_data:
            self.createNode(station,line_data[station],color)

    def addStationEdge(self,stationDict,distance = [], color = "blue"):
        stations = list(stationDict)
        for i in range(len(stations) - 1):
                self.tubeGraph.add_edge(stations[i], stations[i+1], cce=color,label = distance[i])

    # Color generator functions
    def displayKeys(self):
        for line in self.tubeSystem.lines:
            plt.plot([], [], color=line["color"], linewidth=2, label=line["key"])
    
    def setLabelOffset(self,station,x,y,placement):
        dx, dy, ha, va = self.getOffsetAndAlignment(placement)
        x += dx * self.settings.label_x_offset
        y += dy * self.settings.label_y_offset
        self.pltTextStationName(x,y,station,ha,va)

    # Others
    def pltTextStationName(self,x,y,station,ha,va):
        plt.text(x, y, station, ha= ha, va= va,fontsize = self.settings.fontSize)

    def getOffsetAndAlignment(self,key,mode="direction",start_pos =(0,0)):
        if mode == "direction":
            distance = self.settings.distance
            directions = {
                "N":  (0, 1),
                "NE": (1, 1),
                "E":  (1, 0),
                "SE": (1, -1),
                "S":  (0, -1),
                "SW": (-1, -1),
                "W":  (-1, 0),
                "NW": (-1, 1)
            }
            dx, dy = directions.get(key,start_pos)
            return (dx * distance, dy * distance)
        
        else: # For placement
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
            

    """Graph"""
    def createLine(self,line_data,start_pos=(0,0)):
        stations = line_data["station"]
        placeholder = line_data["placeholder"]
        color = line_data["color"]
        directions = line_data["direction"]
        distance = line_data["distance"]
        interchange = line_data["interchange"]
        namePlacement = line_data["placement"]

        station_dict = self.generateStationPos(placeholder, directions,start_pos)

        self.addStationNode(station_dict,color)
        self.addStationEdge(station_dict,distance,color)

    def drawTubeMap(self,figsize = (10,7)):
        plt.figure(figsize=figsize) 


        self.createLine(self.tubeSystem.piccadilly)

        pos = nx.get_node_attributes(self.tubeGraph,'npos')
        nodecolour = nx.get_node_attributes(self.tubeGraph, 'ccn')
        edgecolour = nx.get_edge_attributes(self.tubeGraph, 'cce')
        edge_labels = nx.get_edge_attributes(self.tubeGraph,'label')

        nodeColorArray = nodecolour.values()
        edgeColorArray = edgecolour.values()

        self.displayKeys()
        nx.draw_networkx(self.tubeGraph,pos,node_color = nodeColorArray, with_labels=False)
        nx.draw_networkx_edges(self.tubeGraph,pos,edge_color=edgeColorArray)
        nx.draw_networkx_edge_labels(self.tubeGraph, pos, edge_labels=edge_labels)


        plt.title(self.settings.diagram_name)
        plt.legend(title = self.settings.legend_title,loc = self.settings.legend_location)
        plt.show()

    def test(self,isTest = 0):
        if isTest != 0:
            try: 
                self.drawTubeMap()

            except Exception as error:
                print(f"Error: {error}")
        
        else: 
            self.drawTubeMap()

if __name__ == '__main__':
    tubeMap = TubeMap()
    tubeMap.test(isTest=1)