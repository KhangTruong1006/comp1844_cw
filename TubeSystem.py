class TubeSystem:
    def __init__(self):
        pass

class LineStation(TubeSystem):
    def __init__(self):
        self.piccadilly = ["Hyde Park Corner","Green Park","Piccadilly Circus","Leicester Square","Covent Garden","Holborn"]

class StationNamePosition(TubeSystem):
    def __init__(self):
        # Top - Top Right - Right - Bottom Right - Bottom - Bottom Left - Left - Top Left
        self.piccadilly = ["r","t","t","b","r","l"]

class LineColor(TubeSystem):
    def __init__(self):
        self.piccadilly = ["blue","Picaddilly"]

        self.list= [self.piccadilly]

class Direction(TubeSystem):
    def __init__(self):
        self.piccailly = ["Start","NE","E","E","NE","NE"]

class StationDistance(TubeSystem):
    def __init__(self):
        # In kilometres
        self.piccadilly = [0.81,0.7,0.45,0.33,0.6]