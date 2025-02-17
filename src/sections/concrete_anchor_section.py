from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk, Text

class ConcreteAnchorSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "CONCRETE MASS ANCHOR")
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
            "Level Ground/Slope": {"type": "entry", "unit": "deg"},
            "Dimensions": {"type": "entry", "unit": "m"},
            "Dist Ground to Top": {"type": "entry", "unit": "m"},
            "Dist to A-frame": {"type": "entry", "unit": "m"},
            "Cracks": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Deterioration": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Movement": {"type": "dropdown", "options": ["", "Yes", "No"]}
        }

        self.create_parameter_rows(parameters, columns)