from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk

class FittingsSection(BaseSection):
    def __init__(self, parent, bank="RIGHT"):
        """
        Initialize Fittings section
        
        Args:
            parent: Parent widget
            bank: "RIGHT" or "LEFT" to specify which bank
        """
        super().__init__(parent, f"FITTINGS - {bank} BANK")
        self.create_table()
        self.create_comments()
    
    def create_table(self):
        """Creates the fittings table"""
        columns = ["Parameter", "Main", "Top/Backstay/BTM", "Aircraft Warning"]
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill=tk.X, padx=5, pady=2)
        
        
        for i, col in enumerate(columns):
            ttk.Label(header_frame, text=col, font=('Arial', 9, 'bold')).grid(
                row=0, column=i, padx=5, pady=2
            )

      
        fittings_parameters = {
            "Cable Clamps": {"type": "entry", "unit": "#"},
            "Clamp Torque": {"type": "entry", "unit": "ft-lb"},
            "Turnback Lengths": {"type": "entry", "unit": "m"},
            "Socket": {"type": "dropdown", "options": ["", "Yes", "No", "N/A"]},
            "Movement/Slip": {"type": "entry", "unit": "m"},
            "Rust": {"type": "entry", "unit": "%"},
            "Turnbuckle Size": {"type": "entry", "unit": "in"},
            "Fitting Condition": {"type": "entry", "unit": None},
            "Remaining Adjust": {"type": "entry", "unit": "m"},
            "Clevice (Type)": {"type": "entry", "unit": None},
            "Clevice Condition": {"type": "entry", "unit": None}
        }

        
        self.create_parameter_rows(fittings_parameters, columns)