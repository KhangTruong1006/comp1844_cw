class Setting:
    def __init__(self):
        """Setting"""
        self.fontSize = 8
        self.lineWidth = 2

        self.label_x_offset = 0.4
        self.label_y_offset = 0.3

        self.node_size = 300
        self.node_label_enabled = False

        """Diagram Setting"""
        self.figsize = (15,8) # Width - Height

        self.diagram_name = "London Underground Map"
        self.legend_title = "Key"
        self.legend_location = "lower right"

        self.interchange_station_color = "white"
        self.interchange_border_color = "black"
        