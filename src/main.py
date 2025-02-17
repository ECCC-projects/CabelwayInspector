import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from sections.base_section import BaseSection
from sections.top_section import TopSection
from sections.cables_section import CablesSection
from sections.bridle_cables_section import BridleCablesSection
from sections.fittings_section import FittingsSection
from sections.u_bars_section import UBarsSection  
from sections.concrete_anchor_section import ConcreteAnchorSection
from sections.steel_plate_section import SteelPlateSection
from sections.rock_anchors_section import RockAnchorsSection
from sections.towers_section import TowersSection
from sections.cable_car_section import CableCarSection
from sections.area_section import AreaSection
from sections.aircraft_marker_section import AircraftMarkersSection
from sections.recommendations_section import RecommendationsSection
from components.image_uploader import ImageUploader
from generate.pdf_generator import PDFGenerator
from tkinter import messagebox

class CablewayInspector:
    def __init__(self):
        self.root = TkinterDnD.Tk()
        self.root.title("Cableway Inspection Report Generator")
        self.root.geometry("800x600")
        
        self.sections = {}
        self.images = []

        style = ttk.Style()
        style.configure('Error.TEntry', foreground='red')
        
        self.create_form()
        self.create_image_uploader()
        self.create_export_button()
    
    def create_form(self):
        form_frame = ttk.Frame(self.root)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create scrollable frame
        canvas = tk.Canvas(form_frame)
        scrollbar = ttk.Scrollbar(form_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.sections['top'] = TopSection(scrollable_frame)  
        self.sections['cables'] = CablesSection(scrollable_frame) 
        self.sections['bridle_cables'] = BridleCablesSection(scrollable_frame)
        self.sections['fittings_right'] = FittingsSection(scrollable_frame, "RIGHT")
        self.sections['fittings_left'] = FittingsSection(scrollable_frame, "LEFT")        
        self.sections['ubars_right'] = UBarsSection(scrollable_frame, "RIGHT")
        self.sections['ubars_left'] = UBarsSection(scrollable_frame, "LEFT")
        self.sections['concrete_anchor'] = ConcreteAnchorSection(scrollable_frame)
        self.sections['steel_plate'] = SteelPlateSection(scrollable_frame)
        self.sections['rock_anchors'] = RockAnchorsSection(scrollable_frame)
        self.sections['towers'] = TowersSection(scrollable_frame)
        self.sections['cable_car'] = CableCarSection(scrollable_frame)
        self.sections['area'] = AreaSection(scrollable_frame)
        self.sections['aircraft_markers'] = AircraftMarkersSection(scrollable_frame)
        self.sections['recommendations'] = RecommendationsSection(scrollable_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_image_uploader(self):
        """Create the image upload component"""
        self.image_uploader = ImageUploader(self.root)
    
    def create_export_button(self):
        """Creates the PDF export button"""
        ttk.Button(
            self.root,
            text="Generate PDF Report",
            command=self.generate_pdf
        ).pack(pady=10)

    def generate_pdf(self):
        """Generate PDF report with validation"""
        try:
            # Validate top section
            is_valid, error_messages = self.sections['top'].validate_all()
            
            if not is_valid:
                messagebox.showerror(
                    "Validation Error",
                    "Please correct the following errors:\n" + "\n".join(error_messages)
                )
                return
            
            # Proceed with PDF generation if validation passes
            pdf_generator = PDFGenerator(self.sections, self.image_uploader.get_images())
            filename = pdf_generator.generate()
            
            messagebox.showinfo(
                "Success",
                f"Report generated successfully:\n{filename}"
            )
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred while generating the PDF:\n{str(e)}"
            )
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CablewayInspector()
    app.run()