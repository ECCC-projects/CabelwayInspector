from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk

class AreaSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "AREA")
        self.create_table()
        self.create_comments()
    
    def create_table(self):
        columns = ["Soil Type", "Right Bank", "Left Bank"]
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill=tk.X, padx=5, pady=2)
        
        for i, col in enumerate(columns):
            ttk.Label(header_frame, text=col, font=('Arial', 9, 'bold')).grid(
                row=0, column=i, padx=5, pady=2
            )
        
        area_parameters = {
            "Soil Type (around anchors and footings)": {"type": "entry"},
            "Anchor / footings submerged at high water": {"type": "dropdown", 
            "options": ["", "Yes", "No", "N/A"]},
            "Grass/Trees/Debris": {"type": "entry"},
            "Fence Condition": {"type": "dropdown", 
            "options": ["", "Good", "Fair", "Poor", "N/A"]}
        }
        
        self.create_parameter_rows(area_parameters, columns)