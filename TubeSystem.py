class TubeSystem:
    def __init__(self):
        self.piccadilly = self.lineData(
            "Piccadilly",
            "blue",
            ["p1","p2","p3","p4","p5","p6","p7","p8"],
            ["Hyde Park Corner","Green Park","Piccadilly Circus","Leicester Square","Covent Garden","Holborn","Russell Square","King Cross\n& St Pancras\nInternational"],
            [False,False,False,False,False,True,False,True],
            ["-","NE","E","E","NE","NE","NE","N"],
            ["l","t","t","br","r","r","l","r"],
            [0.81,0.7,0.45,0.33,0.6,0.69,0.84]
        )

        self.central = self.lineData(
            "Central",
            "red",
            ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"],
            ["St Paul's","Chancery Lane","Holborn","Tottenham Court Road","Oxford Circus","Bond Street","Marble Arch","Lancaster Gate","Queensway","Notting Hill Gate"],
            [False,False,True,False,False,False,False,False,False,True],
            ["-","W","NW","NW","W","W","SW","SW","SW","W"],
            ["r","b","r","t","b","t","tl","r","br","l"],
            [1.03,0.63,0.7,0.81,0.49,0.65,1.2,0.83,0.63]
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
