from fpdf import FPDF
from datetime import datetime

class PDFGenerator:
    def __init__(self, sections, images):
        self.sections = sections
        self.images = images
        self.pdf = FPDF()
    
    def generate(self):
        """Generate the complete PDF report"""
        self.pdf.add_page()
        self.add_title()
        self.add_top_section()
        #generic section method for all similar sections
        self._add_generic_section('cables', "CABLES")
        self._add_generic_section('bridle_cables', "BRIDLE CABLES")
        self._add_generic_section('fittings_right', "FITTINGS - RIGHT BANK")
        self._add_generic_section('fittings_left', "FITTINGS - LEFT BANK")
        self._add_generic_section('ubars_right', "U-BARS - RIGHT BANK")
        self._add_generic_section('ubars_left', "U-BARS - LEFT BANK")
        self._add_generic_section('concrete_anchor', "CONCRETE MASS ANCHOR")
        self._add_generic_section('steel_plate', "STEEL PLATE ANCHORS")
        self._add_generic_section('rock_anchors', "ROCK ANCHORS")
        self._add_generic_section('towers', "TOWERS")
        self._add_generic_section('cable_car', "CABLE CAR")
        self._add_generic_section('area', "AREA")
        self._add_generic_section('aircraft_markers', "AIRCRAFT MARKERS")

        self.add_recommendations_section() 
        self.add_images()
        return self.save_pdf()
    
    def add_title(self):
        """Add main title to PDF"""
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(0, 10, "Cableway Inspection Form", ln=True, align='C')
        self.pdf.ln(5)


    def add_top_section(self):
        """Add top section data to PDF"""
        self.pdf.set_font("Arial", size=12)
        
        #Basic info
        for label, widget in self.sections['top'].fields.items():
            if label in ["Station Name", "Station Number", "Date"]:
                self.pdf.set_font("Arial", "B", 10)
                value = widget.get().strip()
                self.pdf.cell(60, 8, f"{label}:", 0)
                self.pdf.set_font("Arial", size=10)
                self.pdf.cell(0, 8, value, ln=True)
        
        #Measurements
        self.pdf.ln(5)
        measurements = {k: v for k, v in self.sections['top'].fields.items() 
                      if k in ["Span", "Sag", "Temperature", "Design Load"]}

        x = self.pdf.get_x()
        y = self.pdf.get_y()
        
        for label, widget in measurements.items():
            value = widget.get().strip()
            unit = "m" if label in ["Span", "Sag"] else "°C" if label == "Temperature" else "kg"
            self.pdf.set_xy(x, y)
            self.pdf.set_font("Arial", "B", 10)
            self.pdf.cell(30, 8, f"{label}:", 0)
            self.pdf.set_font("Arial", size=10)
            self.pdf.cell(20, 8, f"{value} {unit}", 0)
            x += 50
        
        self.pdf.ln(20)
    
    def _add_generic_section(self, section_key, title):
        """Generic method for adding sections to PDF with page break control"""
        #column structures for different sections
        section_columns = {
            'cables': {
                'columns': ["Parameter", "Main", "LB/Backstay/RB", "Aircraft Warning"],
                'widths': [50, 40, 50, 50]
            },
            'bridle_cables': {
                'columns': ["Parameter", "Right Bank", "Left Bank"],
                'widths': [50, 45, 45]
            },
            'fittings_right': {
                'columns': ["Parameter", "Main", "Top/Backstay/BTM", "Aircraft Warning"],
                'widths': [50, 40, 50, 50]
            },
            'fittings_left': {
                'columns': ["Parameter", "Main", "Top/Backstay/BTM", "Aircraft Warning"],
                'widths': [50, 40, 50, 50]
            },
            'ubars_right': {
                'columns': ["Parameter", "Main", "Backstay", "Aircraft Warning"],
                'widths': [50, 40, 40, 50]
            },
            'ubars_left': {
                'columns': ["Parameter", "Main", "Backstay", "Aircraft Warning"],
                'widths': [50, 40, 40, 50]
            },
            'concrete_anchor': {
                'columns': ["Parameter", "Right Bank", "Left Bank"],
                'widths': [50, 45, 45]
            },
            'steel_plate': {
                'columns': ["Parameter", "Right Bank", "Left Bank"],
                'widths': [50, 45, 45]
            },
            'rock_anchors': {
                'columns': ["Parameter", "Right Bank", "Left Bank"],
                'widths': [50, 45, 45]
            },
            'towers': {
                'columns': ["Parameter", "Right Bank", "Left Bank"],
                'widths': [50, 45, 45]
            },
            'cable_car': {
                'columns': ["Parameter", "Value", "Condition"],
                'widths': [50, 45, 45]
            },
            'area': {
                'columns': ["Parameter", "Right Bank", "Left Bank"],
                'widths': [70, 45, 45]
            },
            'aircraft_markers': {
                'columns': ["Parameter", "Value"],
                'widths': [50, 45]
            }
        }

        #estimated height needed for the section
        num_rows = len([k for k in self.sections[section_key].fields.keys() if k != 'comments'])
        row_height = 8  # Height of each row in points
        header_height = 20  # Height for section title and column headers
        estimated_height = (num_rows * row_height) + header_height

        #estimated height for comments if they exist
        if 'comments' in self.sections[section_key].fields:
            comments = self.sections[section_key].fields["comments"].get("1.0", "end-1c").strip()
            num_lines = len(comments.split('\n'))
            estimated_height += (num_lines * row_height) + 15  

        #Check if there's enough space on current page
        space_left = self.pdf.h - self.pdf.get_y() - 20  
        if estimated_height > space_left:
            self.pdf.add_page()

        #Add section title
        self.pdf.ln(10)
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(0, 10, title, ln=True)
        
        #Get column structure for current section
        columns = section_columns[section_key]['columns']
        col_widths = section_columns[section_key]['widths']
        
        #Table header
        self.pdf.set_font("Arial", "B", 10)
        for i, col in enumerate(columns):
            self.pdf.cell(col_widths[i], 8, col, 1)
        self.pdf.ln()
        
        #Table data
        self.pdf.set_font("Arial", size=10)
        for param, row_data in self.sections[section_key].fields.items():
            if param != "comments":
                self.pdf.cell(col_widths[0], 8, param, 1)
                for col in columns[1:]:
                    value = row_data[col].get() if hasattr(row_data[col], 'get') else row_data[col].get()
                    self.pdf.cell(col_widths[columns.index(col)], 8, str(value), 1)
                self.pdf.ln()
        
        
        if "comments" in self.sections[section_key].fields:
            # Check if comments will fit on current page
            comments = self.sections[section_key].fields["comments"].get("1.0", "end-1c").strip()
            num_lines = len(comments.split('\n'))
            comment_height = (num_lines * row_height) + 15  # 15 points for comment header
            
            if (self.pdf.h - self.pdf.get_y() - 20) < comment_height:
                self.pdf.add_page()
            
            self.pdf.ln(5)
            self.pdf.set_font("Arial", "B", 10)
            self.pdf.cell(0, 8, f"{title} COMMENTS:", ln=True)
            self.pdf.set_font("Arial", size=10)
            self.pdf.multi_cell(0, 8, comments)

            
    def add_recommendations_section(self):
        """Add recommendations section to PDF"""
        self.pdf.ln(10)
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(0, 10, "RECOMMENDATIONS", ln=True)
        self.pdf.ln(5)
    
        #recommendations
        self.pdf.set_font("Arial", "B", 10)
        for label, text_widget in self.sections['recommendations'].fields['recommendations'].items():
            self.pdf.cell(0, 8, label, ln=True)
            self.pdf.set_font("Arial", size=10)
            content = text_widget.get("1.0", "end-1c").strip()
            self.pdf.multi_cell(0, 8, content)
            self.pdf.ln(5)
            self.pdf.set_font("Arial", "B", 10)
        
        #inspection details
        self.pdf.ln(10)
        details = self.sections['recommendations'].fields['inspection_details']
        
        #Inspected By line
        self.pdf.cell(100, 8, f"INSPECTED BY: {details['INSPECTED BY'].get()}", 0)
        self.pdf.cell(0, 8, f"DATE: {details['INSPECTED BY_DATE'].get()}", ln=True)
        
        #Reviewed By line
        self.pdf.cell(100, 8, f"REVIEWED BY: {details['REVIEWED BY'].get()}", 0)
        self.pdf.cell(0, 8, f"DATE: {details['REVIEWED BY_DATE'].get()}", ln=True)
        
    
    def add_images(self):
        """Add images to PDF"""
        if self.images:
            self.pdf.add_page()
            self.pdf.set_font("Arial", "B", 16)
            self.pdf.cell(0, 10, "Inspection Images", ln=True, align='C')
            self.pdf.ln(10)
            
            #Calculate dimensions for 3-column layout with margins
            page_width = self.pdf.w
            margin = 15  # Increased margin
            usable_width = page_width - (2 * margin)
            img_width = usable_width / 3  # Equal width for 3 columns
            img_height = img_width * 0.75  #Maintain aspect ratio
            spacing = (usable_width - (3 * img_width)) / 2  #Space between images
            
            x, y = margin, self.pdf.get_y()
            for idx, img_path in enumerate(self.images):
                if idx > 0 and idx % 3 == 0:
                    x = margin
                    y += img_height + 10  #Add spacing between rows
                    
                    if y + img_height > self.pdf.h - margin:
                        self.pdf.add_page()
                        y = margin + 20  #op margin on new page
                
                self.pdf.image(img_path, x, y, img_width, img_height)
                x += img_width + spacing
    
    def save_pdf(self):
        """Save the PDF file"""
        station_name = self.sections['top'].fields["Station Name"].get().strip()
        station_number = self.sections['top'].fields["Station Number"].get().strip()
        date_str = datetime.now().strftime("%Y%m%d")
        filename = f"Inspection_{date_str}_{station_name}_{station_number}.pdf"
        
        self.pdf.output(filename)
        return filename