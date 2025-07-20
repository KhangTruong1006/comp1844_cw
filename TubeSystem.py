class TubeSystem:
    def __init__(self):
        self.piccadilly = self.lineData(
            "Piccadilly",
            "blue",
            ["p1","p2","p3","p4","p5","p6"],
            ["Hyde Park Corner","Green Park","Piccadilly Circus","Leicester Square","Covent Garden","Holborn"],
            [False,False,False,False,False,True],
            ["-","NE","E","E","NE","NE"],
            ["l","t","t","br","r","r"],
            [0.81,0.7,0.45,0.33,0.6]
        )

        self.central = self.lineData(
            "Central",
            "red",
            ["c1","c2","c3","c4","c5","c6","c7","c8"],
            ["Holborn","Tottenham Court Road","Oxford Circus","Bond Street","Marble Arch","Lancaster Gate","Queensway","Notting Hill Gate"],
            [False,False,False,False,False,False,False,True],
            ["-","W","W","W","SW","SW","SW","W"],
            ["r","t","t","t","l","r","b","tl"],
            ["a","a","a","a","a","a","a"]
        )

        self.lines = [self.piccadilly,self.central]

    def lineData(self,key_name,color,placeholder,station,interchange,direction,placement,distance):
        data ={
            "key" : key_name,
            "color" : color,
            "placeholder": placeholder, # Placeholder for station node - id
            "station" : station,        # Station name
            "interchange": interchange, # Interchange Station
            "direction" : direction,    # Station direction
            "placement" : placement,    # Placement of station name
            "distance" : distance       # Distance between stations
        }
        
        return data
