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
    def generateStationPos(self,stations,directions,start_pos = (0,0)):
        pos = {}
        x, y = start_pos
        for i, direction in enumerate(directions):
            dx, dy = self.getOffsetAndAlignment(direction,"direction")
            x += dx
            y += dy
            pos[f'{stations[i]}'] = (x,y)

        return pos

    def labelEdgeDistance(self,edges,distanceList):
        distances = {}
        for i, edge in enumerate(edges):
            distances[edge] = distanceList[i]

        return distances

    def generateEdgeColor(self,color = "blue"):
        edge_colors = []
        for edge in self.tubeGraph.edges():
            edge_colors.append(color)

        return edge_colors
    
    def generateStationColor(self,stations,color = "blue"):
        station_colors ={}
        for station in stations:
            station_colors[station] = color
        
        return station_colors

    def convertToArray(self,dict):
        items = [dict[n] for n in dict]
        return items

    def addStationNode(self,stations):
        for station in stations:
            if station not in self.tubeGraph.nodes():
                self.tubeGraph.add_node(station)

    def addStationEdge(self,stations):
        for i in range(len(stations)-1):
            self.tubeGraph.add_edge(stations[i],stations[i+1])

    def labelStationName(self,stations,pos,placementList):
        for i, station in enumerate(stations):
            x,y = pos[station]
            placement = placementList[i]
            self.setLabelOffset(station,x,y,placement)

    # Color generator functions
    def generateLineColorLegend(self):
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

    def getOffsetAndAlignment(self,key,mode="placement",start_pos =(0,0)):
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
            dx, dy = directions.get(key,start_pos)
            return (dx * distance, dy * distance)

    """Graph"""

    def createLine(self,linedata,start_pos = (0,0)):
        stations = linedata["station"]
        color = linedata["color"]
        directions = linedata["direction"]
        distance = linedata["distance"]
        interchange = linedata["interchange"]
        namePlacement = linedata["placement"]

        self.addStationEdge(stations)
        self.addStationNode(stations)

        pos = self.generateStationPos(stations,directions,start_pos)
        edge_colors = self.generateEdgeColor(color)
        node_colors = self.convertToArray(self.generateStationColor(stations,color))
        edge_distances = self.labelEdgeDistance(self.tubeGraph.edges(),distance)

        self.labelStationName(stations,pos,namePlacement)

        return pos,edge_colors,node_colors,edge_distances
    
    def createSystem(self,system_list):
        all_stations = []
        all_pos = {}
        all_edge_colors = []
        all_node_colors = []
        for system in system_list:
            stations,pos, edge_colors, node_colors = self.createLine(system)
            all_pos.update(pos)
            all_edge_colors.extend(edge_colors)
            all_node_colors.extend(node_colors)
            all_stations.extend(stations)
        
        return all_pos, all_edge_colors,  all_node_colors

    def drawTubeMap(self,figsize = (10,7)):
        plt.figure(figsize=figsize)  

        pos, edge_colors, node_colors, edge_labels = self.createLine(self.tubeSystem.piccadilly)
        
        nx.draw(self.tubeGraph,
                pos,
                node_color = node_colors,
                edge_color = edge_colors)
        
        nx.draw_networkx_edge_labels(self.tubeGraph,pos,edge_labels=edge_labels)

        self.generateLineColorLegend()
        plt.title(self.settings.digram_name)
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