from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk

class RecommendationsSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "RECOMMENDATIONS")
        self.create_recommendations()
        self.create_inspection_details()
    
    def create_recommendations(self):
        """Creates the recommendations area"""
        
        recommendations_frame = ttk.Frame(self.frame)
        recommendations_frame.pack(fill=tk.X, padx=5, pady=5)
        
        
        recommendation_items = [
            "Areas of immediate concern:",
            "Lockout required:",
            "Engineering inspection required:"
        ]
        
        self.fields['recommendations'] = {}
        for item in recommendation_items:
            item_frame = ttk.Frame(recommendations_frame)
            item_frame.pack(fill=tk.X, pady=2)
            
            ttk.Label(item_frame, text=item).pack(anchor='w')
            text_area = tk.Text(item_frame, height=3, width=50)
            text_area.pack(fill=tk.X, pady=2)
            self.fields['recommendations'][item] = text_area
    
    def create_inspection_details(self):
        """Creates the inspection details area"""
        details_frame = ttk.Frame(self.frame)
        details_frame.pack(fill=tk.X, padx=5, pady=10)
        
       
        inspection_items = {
            "INSPECTED BY": {"type": "entry", "date": True},
            "REVIEWED BY": {"type": "entry", "date": True}
        }
        
        self.fields['inspection_details'] = {}
        for label, info in inspection_items.items():
            row_frame = ttk.Frame(details_frame)
            row_frame.pack(fill=tk.X, pady=5)
            
            
            person_frame = ttk.Frame(row_frame)
            person_frame.pack(side=tk.LEFT, expand=True, fill=tk.X)
            ttk.Label(person_frame, text=f"{label}:").pack(side=tk.LEFT, padx=5)
            person_entry = ttk.Entry(person_frame, width=30)
            person_entry.pack(side=tk.LEFT, padx=5)
            
           
            if info.get("date"):
                date_frame = ttk.Frame(row_frame)
                date_frame.pack(side=tk.LEFT, expand=True, fill=tk.X)
                ttk.Label(date_frame, text="DATE:").pack(side=tk.LEFT, padx=5)
                date_entry = ttk.Entry(date_frame, width=20)
                date_entry.pack(side=tk.LEFT, padx=5)
                self.fields['inspection_details'][f"{label}_DATE"] = date_entry
            
            self.fields['inspection_details'][label] = person_entry