from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk, Text

class SteelPlateSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "STEEL PLATE ANCHORS")
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
            "Number of Anchors": {"type": "entry", "unit": None},
            "Horz Rod Angle": {"type": "entry", "unit": "deg"},
            "Stickout Length": {"type": "entry", "unit": "m"},
            "Angle of Ground": {"type": "entry", "unit": "deg"},
            "Dist to A-frame": {"type": "entry", "unit": "m"},
            "Soil Type": {"type": "entry", "unit": None},
            "Anchor Rod Length": {"type": "entry", "unit": "ft"},
            "Rod/Tieback Condition": {"type": "entry", "unit": None}
        }

        self.create_parameter_rows(parameters, columns)