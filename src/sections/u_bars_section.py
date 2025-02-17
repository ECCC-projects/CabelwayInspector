from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk

class UBarsSection(BaseSection):
    def __init__(self, parent, bank="RIGHT"):
        """
        Initialize U-Bars section
        
        Args:
            parent: Parent widget
            bank: "RIGHT" or "LEFT" to specify which bank
        """
        super().__init__(parent, f"U-BARS - {bank} BANK")
        self.create_table()
        self.create_comments()
    
    def create_table(self):
        """Creates the U-Bars table"""
        columns = ["Parameter", "Main", "Backstay", "Aircraft Warning"]
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill=tk.X, padx=5, pady=2)
        
        for i, col in enumerate(columns):
            ttk.Label(header_frame, text=col, font=('Arial', 9, 'bold')).grid(
                row=0, column=i, padx=5, pady=2
            )

        ubars_parameters = {
            "Material (rod,rebar)": {"type": "entry", "unit": None},
            "Diameter": {"type": "entry", "unit": "in"},
            "Distortion/Bending": {"type": "entry", "unit": None},
            "Cracks": {"type": "entry", "unit": None},
            "Connection Condition": {"type": "entry", "unit": None},
            "Rust": {"type": "entry", "unit": None}
        }

        self.create_parameter_rows(ubars_parameters, columns)