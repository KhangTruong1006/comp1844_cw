class Setting:
    def __init__(self):
        """Setting"""
        self.distance = 10
        self.diagonal_distance = 1
        self.angle = 45

        self.fontSize = 8
        self.lineWidth = 2

        self.label_x_offset = 2
        self.label_y_offset = 2

        """Diagram Setting"""
        self.figsize = (12,8) # Width - Height

        self.diagram_name = "London Underground Map"
        self.legend_title = "Key"
        self.legend_location = "lower right"

        self.interchange_station_color = "white"
        self.interchange_node_color = "black"
        