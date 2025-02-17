from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk

class CablesSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "CABLES")
        self.create_table()
        self.create_comments()  
    
    def create_table(self):
        columns = ["Parameter", "Main", "LB/Backstay/RB", "Aircraft Warning"]
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill=tk.X, padx=5, pady=2)
        
        for i, col in enumerate(columns):
            ttk.Label(header_frame, text=col, font=('Arial', 9, 'bold')).grid(
                row=0, column=i, padx=5, pady=2
            )

        cable_parameters = {
            "Diameter": {"type": "entry", "unit": "in"},
            "Angle from Vertical": {"type": "entry", "unit": "deg"},
            "Cable Type": {"type": "dropdown", "options": ["", "Type 1", "Type 2", "Type 3"]},
            "Core Type": {"type": "dropdown", "options": ["", "Type A", "Type B", "Type C"]},
            "Broken Wires": {"type": "entry", "unit": "#"},
            "Pinched Wires": {"type": "entry", "unit": "#"},
            "Broken Strands": {"type": "entry", "unit": "#"},
            "Frays": {"type": "entry", "unit": "%"},
            "Rust": {"type": "entry", "unit": "%"},
            "Distortion": {"type": "dropdown", "options": ["", "Yes", "No", "N/A"]},
            "Pinchage Marks": {"type": "dropdown", "options": ["", "Yes", "No", "N/A"]}
        }

        self.create_parameter_rows(cable_parameters, columns)