from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk

class CableCarSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "CABLE CAR")
        self.create_table()
        self.create_comments()
    
    def create_table(self):
        columns = ["Parameter", "Value", "Condition"]
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill=tk.X, padx=5, pady=2)
        
        for i, col in enumerate(columns):
            ttk.Label(header_frame, text=col, font=('Arial', 9, 'bold')).grid(
                row=0, column=i, padx=5, pady=2
            )

        car_parameters = {
            "Type": {"type": "dropdown", "options": ["", "Detachable/movable"]},
            "Cablecar Material": {"type": "entry", "unit": None},
            "Type of Sheaves": {"type": "entry", "unit": None},
            "Rust/Deterioration": {"type": "entry", "unit": None},
            "Brake": {"type": "dropdown", "options": ["", "Yes", "No"]},
            "Lock": {"type": "dropdown", "options": ["", "Detachable"]}
        }

        self.create_parameter_rows(car_parameters, columns)