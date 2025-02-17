# Cableway Inspector Application

## Overview
The Cableway Inspector is a Python-based desktop application for generating and managing cableway inspection reports. It provides a structured form interface for inputting inspection data and generates standardized PDF reports.

## Features
- Scrollable form for entering inspection data
- Drag-and-drop image upload with preview
- Backup file upload button for images
- Automatic PDF generation with a structured layout
- Modular architecture for easy maintenance and expansion
- Validation feature: Station Name and Station Number are required fields, and the date must be in the correct format.

## Installation
### Prerequisites
Ensure you have Python installed. Then, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ECCC-projects/CabelwayInspector.git
   cd CabelwayInspector
   ```
2. Install required libraries:
   ```bash
   pip install pillow
   pip install fpdf
   pip install tkinterdnd2
3. Run the application:
   ```bash
   cd src
   python main.py
   ```

## Usage
1. Launch the application.
2. Fill in the form sections:
   - Top section (basic information)
   - Various inspection sections
   - Recommendations
3. Add images (optional):
   - Drag and drop images directly
   - Use upload button for file selection
   - Supported formats: PNG, JPG, JPEG, GIF, BMP
4. Click the **Generate PDF** button to create a report.
5. The generated PDF will be saved with an auto-generated filename based on the current date, Station Name, and Station Number.

## Assumptions
- Users will enter valid inspection data without additional enforcement beyond the implemented validation.
- The application will be used in an environment where Python 3.8+ is available.
- The generated PDFs will be stored in the src directory.

## Directory Structure
```
src/
├── components/
│   └── image_uploader.py
├── sections/
│   ├── base_section.py
│   ├── top_section.py
│   ├── cables_section.py
│   ├── bridle_cables_section.py
│   ├── fittings_section.py
│   ├── u_bars_section.py
│   ├── concrete_anchor_section.py
│   ├── steel_plate_section.py
│   ├── rock_anchors_section.py
│   ├── towers_section.py
│   ├── cable_car_section.py
│   └── recommendations_section.py
└── generate/
    └── pdf_generator.py
```

## Future Steps 
1. Data Management and Persistence
   - Save form progress
   - Create a data backup and recovery system
2. Performance:
   - Implement caching mechanisms
   - PDF generation speed
3. Integration Capabilities
   - Create export/import interfaces for different file formats
 
   
## Dependencies
- `tkinter` – GUI framework
- `tkinterdnd2` – Drag-and-drop functionality
- `PIL` – Image handling
- `FPDF` – PDF generation


