import tkinter as tk
from tkinter import ttk, Text

class BaseSection:
    def __init__(self, parent, title):
        """
        Base class for all form sections
        
        Args:
            parent: Parent tkinter widget
            title: Section title
        """
        self.parent = parent
        self.title = title
        self.frame = None
        self.fields = {}
        
        self.create_section()
    
    def create_section(self):
        """Creates the basic section frame"""
        self.frame = ttk.LabelFrame(self.parent, text=self.title)
        self.frame.pack(fill=tk.X, padx=5, pady=5)


    def create_comments(self):
        """Creates the comments section"""
        comments_frame = ttk.Frame(self.frame)
        comments_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Label(comments_frame, text="COMMENTS:").pack(anchor='w')
        comments = Text(comments_frame, height=3, width=50)
        comments.pack(fill=tk.X, pady=2)
        self.fields["comments"] = comments

    def create_parameter_rows(self, parameters, columns):
        """Helper method to create parameter rows"""
        for param, info in parameters.items():
            row_frame = ttk.Frame(self.frame)
            row_frame.pack(fill=tk.X, padx=5, pady=1)
        
            ttk.Label(row_frame, text=param).grid(
                row=0, column=0, padx=5, pady=2, sticky='w'
            )
        
            row_fields = {}
            for col_idx, col in enumerate(columns[1:], start=1):
                if info["type"] == "dropdown":
                    widget = ttk.Combobox(
                    row_frame, 
                    values=info["options"], 
                    width=15, 
                    state="readonly"
                )
                    widget.grid(row=0, column=col_idx, padx=5, pady=2)
                else:
                    frame = ttk.Frame(row_frame)
                    frame.grid(row=0, column=col_idx, padx=5, pady=2)
                    widget = ttk.Entry(frame, width=10)
                    widget.pack(side=tk.LEFT)
                    if "unit" in info and info["unit"]:
                        ttk.Label(frame, text=info["unit"]).pack(side=tk.LEFT)
            
                row_fields[col] = widget
        
            self.fields[param] = row_fields

    