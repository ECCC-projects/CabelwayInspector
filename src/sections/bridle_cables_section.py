from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk

class BridleCablesSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "BRIDLE CABLES")
        self.create_table()
        self.create_comments()  # Now using base class method
    
    def create_table(self):
        columns = ["Parameter", "Right Bank", "Left Bank"]
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill=tk.X, padx=5, pady=2)
        
        for i, col in enumerate(columns):
            ttk.Label(header_frame, text=col, font=('Arial', 9, 'bold')).grid(
                row=0, column=i, padx=5, pady=2
            )

        bridle_parameters = {
            "Cable Type": {"type": "dropdown", "options": ["", "Type 1", "Type 2", "Type 3"]},
            "Diameter": {"type": "entry", "unit": "in"},
            "Cable Clamps": {"type": "entry", "unit": "#"},
            "Spread Angle": {"type": "entry", "unit": "deg"}
        }

        self.create_parameter_rows(bridle_parameters, columns)