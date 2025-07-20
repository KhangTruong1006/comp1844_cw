class TubeSystem:
    def __init__(self):
        self.piccadilly = self.lineData(
            "Piccadilly",
            "blue",
            [0,1,2,2,1,1,1,1],
            ["Hyde Park Corner","Green Park","Piccadilly Circus","Leicester Square","Covent Garden","Holborn","Russell Square","King Cross\n& St Pancras\nInternational"],
            [False,False,False,False,False,True,False,False],
            ["-","NE","E","E","NE","NE","NE","N"],
            ["l","l","t","br","l","r","l","r"],
            [0.81,0.7,0.45,0.33,0.6,0.69,0.84]
        )

        self.central = self.lineData(
            "Central",
            "red",
            [0,2,1,2,2,4,1,1,1,2],
            ["St Paul's","Chancery Lane","Holborn","Tottenham Court Road","Oxford Circus","Bond Street","Marble Arch","Lancaster Gate","Queensway","Notting Hill Gate"],
            [False,False,True,False,False,False,False,False,False,False],
            ["-","W","NW","W","W","W","SW","SW","SW","W"],
            ["r","b","r","t","b","t","tl","r","br","l"],
            [1.03,0.63,0.7,0.81,0.49,0.65,1.2,0.83,0.63]
        )

        self.jubilee = self.lineData(
            "Jubilee",
            "gray",
            [0,2,2,1,2,2,2],
            ["Bond Street","Green Park","Westminster","Waterloo","Southwark","London Bridge","Bermondsey"],
            [True,True,False,False,False,False,False],
            ["-","SE","SE","SE","E","NE","E"],
            ["t","l","l","l","b","tl","b"],
            ["A","A","A","A","A","A"]
        )

        self.lines = [self.piccadilly,self.central,self.jubilee]

    def lineData(self,key_name,color,node_distance,station,interchange,direction,placement,distance):
        data ={
            "key" : key_name,
            "color" : color,
            "node_distance": node_distance, # Distance between nodes
            "station" : station,            # Station name
            "interchange": interchange,     # Interchange Station
            "direction" : direction,        # Station direction
            "placement" : placement,        # Placement of station name
            "distance" : distance,          # Distance between stations
            "placeholder": self.generatePlacehoderStation(key_name[0],station)  # Placeholder for station node
        }
        
        return data

    def generatePlacehoderStation(self,placeholder,station):
        array = []
        for i in range(len(station)):
            array.append(f'{placeholder}{i}')

        return array