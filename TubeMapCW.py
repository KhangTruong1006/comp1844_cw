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
                "NE": (1, 1),
                "E":  (1, 0),
                "SE": (1, -1),
                "S":  (0, -1),
                "SW": (-1,-1),
                "W":  (-1, 0),
                "NW": (-1, 1)
            }
            dx, dy = directions.get(key,start_pos)
            return (dx * distance, dy * distance)

    """Graph"""

    def createLine(self,linedata,start_pos = (0,0)):
        station = linedata["station"]
        color = linedata["color"]
        direction = linedata["direction"]
        distance = linedata["distance"]
        interchange = linedata["interchange"]
        namePlacement = linedata["placement"]

        
      
        return 1
    
    

    def drawTubeMap(self,figsize = (10,7)):
        plt.figure(figsize=figsize)  
        
        
        self.generateLineColorLegend()
        plt.title(self.settings.digram_name)
        plt.legend(title = self.settings.legend_title,loc = self.settings.legend_location)
        plt.show()

    def test(self,isTest = 0):
        if isTest == 0:
            try: 
                self.drawTubeMap()

            except Exception as error:
                print(f"Error: {error}")
        
        else: 
            self.drawTubeMap()

if __name__ == '__main__':
    tubeMap = TubeMap()
    tubeMap.test(isTest=0)