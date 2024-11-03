# pip install Pillow
# pip install pytesseract

import tkinter as tk
from tkinter import font as tkFont, filedialog
from PIL import Image, ImageTk

# Function to choose an image
def choose_image():
    global chosen_image_path
    chosen_image_path = filedialog.askopenfilename(title="Choose an Image", filetypes=[("Image Files", ".png;.jpg;*.jpeg")])
    if chosen_image_path:
        image_label.config(text=f"Selected Image: {chosen_image_path}")
    else:
        image_label.config(text="No image selected")

# Function to open the Encrypt window
def open_encrypt_window():
    encrypt_window = tk.Toplevel(root)
    encrypt_window.title("Encrypt")
    encrypt_window.geometry("800x500")
    encrypt_window.configure(bg='black')

    # Choose Image Button
    choose_image_button = tk.Button(encrypt_window, text="Choose Image", command=choose_image, bg='#3d85c6', fg='white', font=('Times New Roman', 14))
    choose_image_button.pack(pady=10)

    # Secret Key Entry for encryption
    secret_key_entry_encrypt = tk.Entry(encrypt_window, width=30, font=('Times New Roman', 14))
    secret_key_entry_encrypt.pack(pady=10)
    secret_key_entry_encrypt.insert(0, "Enter Secret Key for Encryption")

    # Encrypt Button 
    encrypt_button = tk.Button(encrypt_window, text="Encrypt", bg='#3d85c6', fg='white', font=('Times New Roman', 14))
    encrypt_button.pack(pady=10)

    # Label to display the selected image path
    global image_label
    image_label = tk.Label(encrypt_window, text="No image selected", bg='black', fg='white', font=("Arial", 12))
    image_label.pack(pady=5)

    # Large Textbox for encrypted text output
    encrypted_text_box = tk.Text(encrypt_window, wrap="word", width=40, height=10, font=("Arial", 12))
    encrypted_text_box.pack(pady=10)
    encrypted_text_box.insert("1.0", "Encrypted text will appear here...")  # Optional placeholder text

    # Exit Button
    back_button = tk.Button(encrypt_window, text="Exit", command=encrypt_window.destroy, bg='#3d85c6', fg='white', font=('Times New Roman', 14))
    back_button.pack(pady=20)

# Function to open the Decrypt window
def open_decrypt_window():
    decrypt_window = tk.Toplevel(root)
    decrypt_window.title("Decrypt")
    decrypt_window.geometry("400x300")
    decrypt_window.configure(bg='black')

    # Exit Button for Decrypt window
    back_button = tk.Button(decrypt_window, text="Exit", command=decrypt_window.destroy, bg='#3d85c6', fg='white', font=('Times New Roman', 14))
    back_button.pack(pady=20)

# Create the main application window
root = tk.Tk()
root.title("Image Encryption")
root.geometry("700x400")
root.configure(bg='black')

# Set custom font for the label and buttons
font_style = tkFont.Font(family="Times New Roman", size=20, weight="bold")
button_font_style = tkFont.Font(family="Times New Roman", size=16)

# Create a label for the title
title_label = tk.Label(root, text="IMAGE <=======> TEXT", bg='black', fg='#3d85c6', font=font_style)
title_label.pack(pady=(50, 20))  # Center title label with padding

# Create a frame to hold the buttons
button_frame = tk.Frame(root, bg='black')
button_frame.pack(pady=(10, 0))  # Reduced padding to center the buttons below the title

# Create Encrypt button
encrypt_button = tk.Button(button_frame, text="Encrypt", command=open_encrypt_window, bg='#3d85c6', fg='white', font=button_font_style, width=15, height=3)
encrypt_button.pack(side=tk.LEFT, padx=(0, 5))  # Small space to the right

# Create Decrypt button
decrypt_button = tk.Button(button_frame, text="Decrypt", command=open_decrypt_window, bg='#3d85c6', fg='white', font=button_font_style, width=15, height=3)
decrypt_button.pack(side=tk.LEFT, padx=(5, 0))  # Small space to the left

# Initialize chosen image path variable
chosen_image_path = None

# Run the main event loop
root.mainloop()
