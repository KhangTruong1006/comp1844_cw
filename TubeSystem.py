class TubeSystem:
    def __init__(self):
        self.piccadilly = self.lineData(
            "Piccadilly",
            "blue",
            ["Hyde Park Corner","Green Park","Piccadilly Circus","Leicester Square","Covent Garden","Holborn"],
            [False,False,False,False,False,True],
            ["-","NE","E","E","NE","NE"],
            ["l","t","t","b","r","r"],
            [0.81,0.7,0.45,0.33,0.6]
        )

        self.central = self.lineData(
            "Central",
            "red",
            ["Holborn","Tottenham Court Road","Oxford Circus","Bond Street","Marble Arch","Lancaster Gate"],
            [True,False,False,False,False,False],
            ["-","W","W","W","SW","SW"],
            ["r","t","t","b","r","l"],
            ["a","a","a","a","a"]
        )

        self.lines = [self.piccadilly,self.central]

    def lineData(self,key_name,color,station,interchange,direction,placement,distance):
        data ={
            "key" : key_name,
            "color" : color,
            "station" : station,        # Station name
            "interchange": interchange, # Interchange Station
            "direction" : direction,    # Station direction
            "placement" : placement,    # Placement of station name
            "distance" : distance       # Distance between stations
        }
        
        return data
