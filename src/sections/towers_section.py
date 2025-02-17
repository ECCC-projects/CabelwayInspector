from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk

class TowersSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "TOWERS")
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

        tower_parameters = {
            "Frame Type": {"type": "entry", "unit": None},
            "Height": {"type": "entry", "unit": "m"},
            "Width at Base": {"type": "entry", "unit": "m"},
            "Tower Material": {"type": "entry", "unit": None},
            "Base Type": {"type": "dropdown", "options": ["", "Type 1", "Type 2", "Type 3"]},
            "Base Condition": {"type": "entry", "unit": None},
            "Footing Type": {"type": "entry", "unit": None},
            "Footing Dimensions": {"type": "entry", "unit": "m"},
            "Footing abground": {"type": "entry", "unit": "m"},
            "Rust": {"type": "entry", "unit": None},
            "Cracks": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Plumb": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Ladder Condition": {"type": "entry", "unit": None},
            "Decking Condition": {"type": "entry", "unit": None},
            "Railing Condition": {"type": "entry", "unit": None},
            "Platform Safety Chain": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Safety Loop": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Decking hook": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Danger Sign": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Cable Support Type": {"type": "dropdown", "options": ["", "channel", "saddle block", "pipe guide rig"]},
            "Support Condition": {"type": "entry", "unit": None},
            "Welds": {"type": "entry", "unit": None}
        }

        self.create_parameter_rows(tower_parameters, columns)