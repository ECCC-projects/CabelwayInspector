from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk

class AircraftMarkersSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "AIRCRAFT MARKERS")
        self.create_table()
        self.create_comments()
    
    def create_table(self):
        columns = ["Parameter", "Value"]
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill=tk.X, padx=5, pady=2)
        
        for i, col in enumerate(columns):
            ttk.Label(header_frame, text=col, font=('Arial', 9, 'bold')).grid(
                row=0, column=i, padx=5, pady=2
            )
        
        aircraft_markers_parameters = {
            "Type": {"type": "dropdown", 
            "options": ["", "Permanent", "Temporary", "Movable", "N/A"]},
            "Number": {"type": "entry"},
            "Condition": {"type": "dropdown", 
            "options": ["", "Excellent", "Good", "Fair", "Poor", "N/A"]}
        }
        
        self.create_parameter_rows(aircraft_markers_parameters, columns)
    