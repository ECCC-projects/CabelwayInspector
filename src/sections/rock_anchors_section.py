from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk, Text

class RockAnchorsSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "ROCK ANCHORS")
        self.create_table()
        self.create_comments()
    
    def create_table(self):
        columns = ["Parameter", "Right Bank", "Left Bank"]
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill=tk.X, padx=5, pady=2)
        
        for i, col in enumerate(columns):
            ttk.Label(header_frame, text=col, font=('Arial', 9, 'bold')).grid(
                row=0, column=i, padx=5, pady=2
            )

        parameters = {
            "No.of Anchors - main": {"type": "entry", "unit": None},
            "Angle of Pull - main": {"type": "entry", "unit": "deg"},
            "Rod Material - main": {"type": "entry", "unit": None},
            "Anchor(s) dia - main": {"type": "entry", "unit": "in"},
            "Anchor Condition - main": {"type": "entry", "unit": None},
            "Grout": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Rock Type": {"type": "entry", "unit": None},
            "Anchor Movement": {"type": "entry", "unit": None},
            "Marker Anchor": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Rock Fractures": {"type": "entry", "unit": None}
        }

        self.create_parameter_rows(parameters, columns)