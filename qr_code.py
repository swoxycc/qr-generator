import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk
import os

# Create the main application class
class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x600")  # Set window size

        # Create input field for URL
        self.url_label = ctk.CTkLabel(root, text="Enter URL:")
        self.url_label.pack(pady=10)

        self.url_entry = ctk.CTkEntry(root, width=300)
        self.url_entry.pack(pady=10)

        # Create button to generate QR code
        self.generate_button = ctk.CTkButton(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        # Placeholder for the QR code image
        self.qr_image = None
        self.qr_image_label = ctk.CTkLabel(root)
        self.qr_image_label.pack(pady=10)

    def generate_qr_code(self):
        url = self.url_entry.get()
        if url:
            # Generate QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            self.qr_image = qr.make_image(fill_color="black", back_color="white")

            # Save the image temporarily to display it
            self.qr_image.save("qr.png")

            # Display the QR code in the GUI
            self.display_qr_code()

    def display_qr_code(self):
        # Convert the QR code image to a format that can be displayed in the GUI
        self.qr_image = self.qr_image.convert("RGB")  # Convert to RGB
        self.qr_image_tk = ImageTk.PhotoImage(self.qr_image)  # Create PhotoImage

        # Update the label with the QR code image
        self.qr_image_label.configure(image=self.qr_image_tk)
        self.qr_image_label.image = self.qr_image_tk  # Keep a reference to avoid garbage collection

    def save_qr_code(self):
        if self.qr_image:
            # Save the QR code as qr.png in the current directory
            self.qr_image.save("qr.png")  
            print("QR code saved as qr.png")

# Run the application
if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

    root = ctk.CTk()  # Create the main window
    app = QRCodeApp(root)  # Initialize the application
    root.mainloop()  # Start the main loop 
