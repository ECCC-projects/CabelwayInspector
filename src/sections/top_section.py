from .base_section import BaseSection
import tkinter as tk
from tkinter import ttk, messagebox
from utils.validators import validate_date, validate_required_field, ValidationError

class TopSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, "Cableway Inspection Form")
        self.error_labels = {}  #Store error labels for fields
        self.create_basic_info()
        self.create_measurements()
        
    def create_basic_info(self):
        basic_info = {
            "Station Name": {"type": "entry", "unit": None, "required": True},
            "Station Number": {"type": "entry", "unit": None, "required": True},
            "Date": {"type": "entry", "unit": None, "required": True, "validate": "date"}
        }
        
        basic_fields = {}
        for label, field_info in basic_info.items():
            frame = ttk.Frame(self.frame)
            frame.pack(fill=tk.X, padx=5, pady=2)
            
            
            ttk.Label(frame, text=f"{label}:").pack(side=tk.LEFT)
            
            
            widget = ttk.Entry(frame, width=40)
            widget.pack(side=tk.LEFT, padx=5)
            
            #Add validation binding
            if field_info.get("validate") == "date":
                widget.bind('<FocusOut>', lambda e, w=widget, l=label: self.validate_field(w, l))
            elif field_info.get("required"):
                widget.bind('<FocusOut>', lambda e, w=widget, l=label: self.validate_required(w, l))
            
            #Error label (hidden by default)
            error_label = ttk.Label(frame, text="", foreground="red")
            error_label.pack(side=tk.LEFT, padx=5)
            self.error_labels[label] = error_label
            
            basic_fields[label] = widget
            
        self.fields.update(basic_fields)

    def validate_field(self, widget, field_name):
        """Validate individual field"""
        value = widget.get().strip()
        
        if field_name == "Date":
            is_valid, error_msg = validate_date(value)
        else:
            is_valid, error_msg = validate_required_field(value, field_name)
        
        #Show/hide error message
        error_label = self.error_labels[field_name]
        if not is_valid:
            error_label.config(text=error_msg)
            widget.config(style='Error.TEntry')  #Add red border
        else:
            error_label.config(text="")
            widget.config(style='TEntry')  #Reset to normal style
        
        return is_valid

    def validate_required(self, widget, field_name):
        """Validate required fields"""
        value = widget.get().strip()
        is_valid, error_msg = validate_required_field(value, field_name)
        
        #Show/hide error message
        error_label = self.error_labels[field_name]
        if not is_valid:
            error_label.config(text=error_msg)
            widget.config(style='Error.TEntry')
        else:
            error_label.config(text="")
            widget.config(style='TEntry')
        
        return is_valid

    def validate_all(self):
        """
        Validate all fields in the section
        Returns: (bool, list) - (all_valid, error_messages)
        """
        all_valid = True
        error_messages = []
        
        for label, widget in self.fields.items():
            if label in ["Station Name", "Station Number"]:
                is_valid = self.validate_required(widget, label)
            elif label == "Date":
                is_valid = self.validate_field(widget, label)
            else:
                continue
                
            if not is_valid:
                all_valid = False
                error_messages.append(f"Invalid {label}")
        
        return all_valid, error_messages

    def create_measurements(self):
        """Creates the measurement fields"""
        measurements = {
            "Span": {"type": "entry", "unit": "m"},
            "Sag": {"type": "entry", "unit": "m"},
            "Temperature": {"type": "entry", "unit": "°C"},
            "Design Load": {"type": "entry", "unit": "kg"}
        }
        
        measurement_frame = ttk.Frame(self.frame)
        measurement_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for label, field_info in measurements.items():
            frame = ttk.Frame(measurement_frame)
            frame.pack(side=tk.LEFT, padx=5)
            
            ttk.Label(frame, text=f"{label}:").pack(side=tk.LEFT)
            widget = ttk.Entry(frame, width=10)
            widget.pack(side=tk.LEFT, padx=2)
            ttk.Label(frame, text=field_info["unit"]).pack(side=tk.LEFT)
            self.fields[label] = widget
