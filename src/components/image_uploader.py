import tkinter as tk
from tkinter import ttk, filedialog
from tkinterdnd2 import DND_FILES
from PIL import Image, ImageTk

class ImageUploader:
    def __init__(self, parent):
        """
        Initialize the image uploader component
        
        Args:
            parent: Parent tkinter widget
        """
        self.parent = parent
        self.images = []
        self.create_upload_area()
        
    def create_upload_area(self):
        """Creates the image upload area with drag-and-drop support"""
        self.upload_frame = ttk.LabelFrame(self.parent, text="Drop Images Here")
        self.upload_frame.pack(fill=tk.X, padx=10, pady=5)
        
        #Configure drag and drop
        self.upload_frame.drop_target_register(DND_FILES)
        self.upload_frame.dnd_bind('<<Drop>>', self.handle_drop)
        
        #Add upload button
        ttk.Button(
            self.upload_frame,
            text="Upload Images",
            command=self.upload_images
        ).pack(pady=10)
        
        #display area for thumbnails
        self.image_display = ttk.Frame(self.upload_frame)
        self.image_display.pack(fill=tk.X, pady=5)
    
    def handle_drop(self, event):
        """Handle drag and drop events"""
        files = self.parent.tk.splitlist(event.data)
        self.process_images(files)
    
    def upload_images(self):
        """Handle manual image upload via button"""
        files = filedialog.askopenfilenames(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        self.process_images(files)
    
    def process_images(self, files):
        """Process uploaded images and display thumbnails"""
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.images.append(file)
                
                #display thumbnail
                img = Image.open(file)
                img.thumbnail((100, 100))
                photo = ImageTk.PhotoImage(img)
                
                label = ttk.Label(self.image_display, image=photo)
                label.image = photo  # Keep a reference
                label.pack(side=tk.LEFT, padx=5)
    
    def get_images(self):
        """Return list of uploaded image paths"""
        return self.images