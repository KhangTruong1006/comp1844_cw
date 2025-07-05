class TubeSystem:
    def __init__(self):
        pass

class LineStation(TubeSystem):
    def __init__(self):
        self.piccadilly = ["Hyde Park Corner","Green Park","Piccadilly Circus","Leicester Square","Covent Garden","Holborn"]

class LineColor(TubeSystem):
    def __init__(self):
        self.piccadilly = ["blue","Picaddilly"]

        self.list= [self.piccadilly]

class Direction(TubeSystem):
    def __init__(self):
        self.piccailly = ["Start","NE","E","E","NE","NE"]

class StationDistance(TubeSystem):
    def __init__(self):
        self.piccadilly = ["a","b","c","d","e"]