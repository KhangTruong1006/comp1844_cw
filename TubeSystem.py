class TubeSystem:
    def __init__(self):
        self.piccadilly = self.lineData(
            "Piccadilly",
            "navy",
            (-1,-1),
            [0,2,3,3,1,1],
            ["Hyde Park Corner","Green Park","Piccadilly Circus","Leicester Square","Covent Garden","Holborn"],
            [False,True,True,False,False,True],
            ["-","NE","E","E","NE","NE"],
            ["l","tr","tr","br","l","r"],
            [0.81,0.7,0.45,0.33,0.6]
        )

        self.central = self.lineData(
            "Central",
            "red",
            (12,2),
            [0,2,1,2,5,3,2,1,1,2],
            ["St Paul's","Chancery Lane","Holborn","Tottenham Court Road","Oxford Circus","Bond Street","Marble Arch","Lancaster Gate","Queensway","Notting Hill Gate"],
            [False,False,True,False,True,True,False,False,False,False],
            ["-","W","NW","W","W","W","SW","SW","SW","W"],
            ["r","b","r","t","tr","tl","tl","r","b","l"],
            [1.03,0.63,0.7,0.81,0.49,0.65,1.2,0.83,0.63]
        )

        self.jubilee = self.lineData(
            "Jubilee",
            "lightslategray",
            (-1,8),
            [0,2,3,2,2.5,1.5,3,2,2],
            ["St John's Wood","Baker Street","Bond Street","Green Park","Westminster","Waterloo","Southwark","London Bridge","Bermondsey"],
            [False,True,True,True,False,True,False,False,False],
            ["-","S","S","SE","SE","SE","E","NE","E"],
            ["tr","tr","tl","tr","l","l","b","tl","b"],
            [1.75,1.7,1.17,1.4,0.81,0.55,1.26,1.98]
        )
        
        self.bakerloo = self.lineData(
            "Bakerloo",
            "brown",
            (-3,8),
            [0,2,1.5,1.5,2,1,1.5,1.5,2,],
            ["Marylebone","Baker Street","Regent's Park","Oxford Circus","Piccadilly Circus","Charing Cross","Embankment","Waterloo","Lambeth North"],
            [False,True,False,True,True,False,False,True,False],
            ["-","SE","SE","SE","SE","SE","S","S","S"],
            ["t","tr","r","tr","tr","br","r","l","r"],
            [0.43,0.72,1,0.94,0.57,0.38,0.7,0.52]
        )

        self.lines = [self.bakerloo,self.central,self.jubilee,self.piccadilly]

    def lineData(self,key_name,color,start,node_distance,station,interchange,direction,placement,distance):
        data ={
            "key" : key_name,
            "color" : color,
            "start": start,
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