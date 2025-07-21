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

        self.tubeGraph = nx.Graph()

        self.keys = []

    """Functions"""
    # Add functions
    def addStationNode(self,line_data,interchange,color = "blue"):
        for i,station in enumerate(line_data):
            if interchange[i] != True:
                self.createNode(station, line_data[station], color, color)
            else:
                self.createNode(station, line_data[station], self.settings.interchange_station_color)
    
    def addStationEdge(self,stationDict,distance = [], color = "blue"):
        stations = list(stationDict)
        for i in range(len(stations) - 1):
            self.tubeGraph.add_edge(stations[i], stations[i+1], ecl=color,label = distance[i])

    # Display functions
    def displayKeys(self):
        for key in self.keys:
            plt.plot([], [], color=key["color"], linewidth=2, label=key["key"])
            
    def displayStationName(self,station_dict,names,placement):
        for i,(x,y) in enumerate(station_dict.values()):
            dx,dy, ha, va = self.getOffsetAndAlignment(placement[i],"placement",(x,y))
            x += dx * self.settings.label_x_offset
            y += dy * self.settings.label_y_offset
            self.pltTextStationName(x,y,names[i],ha,va)
            
    # Helper functions
    def createNode(self,name,pos,color = "blue", node_edge = "black"):
        self.tubeGraph.add_node(name,npos = pos, ncl= color, nbc = node_edge)
        
    def pltTextStationName(self,x,y,station,ha,va):
        plt.text(x, y, station, ha= ha, va= va,fontsize = self.settings.fontSize)
    
    def generateStationPos(self,placeholders,node_pos,directions,start_pos = (0,0)):
        pos= {}
        x, y = start_pos
        for i, direction in enumerate(directions):
            dx, dy = self.getOffsetAndAlignment(direction,node_pos[i],"direction")
            x += dx
            y += dy
            pos[f'{placeholders[i]}'] = (x,y)

        return pos
     
    def getOffsetAndAlignment(self,key,distance = 1,mode="direction",start_pos = (0,0)):
        if mode == "direction":
            directions = {
                "N":  (0, 1),
                "NE": (1, 1),
                "E":  (1, 0),
                "SE": (1,-1),
                "S":  (0,-1),
                "SW": (-1,-1),
                "W":  (-1,0),
                "NW": (-1,1)
            }
            dx, dy = directions.get(key,start_pos)
            return (dx * distance, dy * distance)
        
        else: # For placement
            offsets = {
                "t":   (0, 1,'center', 'bottom'),
                "tr":  (0.5, 1,'left', 'bottom'),
                "r":   (1, 0,'left', 'center'),
                "br":  (1, -1,'left', 'bottom'),
                "b":   (0, -1,'center', 'top'),
                "bl":  (-1,-1,'right', 'bottom'),
                "l":   (-1, 0,'right', 'center'),
                "tl":  (-1, 1,'right', 'bottom')
            }
            dx, dy, ha, va = offsets.get(key, (0,0,'center', 'center'))
            return (dx,dy, ha, va)
     
    """Graph"""
    def createLine(self,line_data):
        stations = line_data["station"]
        placeholder = line_data["placeholder"]
        color = line_data["color"]
        directions = line_data["direction"]
        distance = line_data["distance"]
        interchange = line_data["interchange"]
        namePlacement = line_data["placement"]
        nodeDistance = line_data["node_distance"]
        start_pos = line_data["start"]

        self.keys.append(line_data)
        station_dict = self.generateStationPos(placeholder, nodeDistance,directions,start_pos)

        self.addStationNode(station_dict,interchange,color)
        self.addStationEdge(station_dict,distance,color)
        self.displayStationName(station_dict,stations,namePlacement)

    def Task_1(self):
        plt.figure(figsize= self.settings.figsize) 
        self.createLine(self.tubeSystem.piccadilly)
        
        self.drawTubeMap()
        
    def Task_2(self):
        plt.figure(figsize= self.settings.figsize)
        self.createLine(self.tubeSystem.piccadilly)
        self.createLine(self.tubeSystem.central)
        self.createLine(self.tubeSystem.jubilee)
        self.createLine(self.tubeSystem.bakerloo)
        
        self.drawTubeMap()
    
    def drawTubeMap(self):
        pos = nx.get_node_attributes(self.tubeGraph,'npos')
        nodeColor = nx.get_node_attributes(self.tubeGraph, 'ncl')   # ncl - Node Color
        nodeBorder = nx.get_node_attributes(self.tubeGraph, 'nbc')  # nbc - Node Border Color - mostly for interchange station
        edgeColor = nx.get_edge_attributes(self.tubeGraph, 'ecl')   # ecl - Edge Color
        edge_labels = nx.get_edge_attributes(self.tubeGraph,'label')# Edge Label

        nodeColorArray = list(nodeColor.values())
        nodeBorderArray = list(nodeBorder.values())
        edgeColorArray = list(edgeColor.values())

        self.displayKeys()
        nx.draw(self.tubeGraph,
                pos,node_size = self.settings.node_size,
                node_color = nodeColorArray,
                edgecolors=nodeBorderArray, 
                with_labels=self.settings.node_label_enabled)
        
        nx.draw_networkx_edges(self.tubeGraph,pos,edge_color=edgeColorArray)
        nx.draw_networkx_edge_labels(self.tubeGraph, pos, edge_labels=edge_labels)

        plt.title(self.settings.diagram_name)
        plt.legend(title = self.settings.legend_title,loc = self.settings.legend_location)
        plt.show()

if __name__ == '__main__':
    try: 
        run = TubeMap()
        # run.Task_1()
        run.Task_2()

    except Exception as error:
        print(f"Error: {error}")