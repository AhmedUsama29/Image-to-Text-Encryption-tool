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

# Function to show the encryption frame
def show_encrypt_frame():
    encrypt_frame.pack(fill="both", expand=True)
    decrypt_frame.pack_forget()  # Hide the decrypt frame

# Function to show the decryption frame
def show_decrypt_frame():
    decrypt_frame.pack(fill="both", expand=True)
    encrypt_frame.pack_forget()  # Hide the encrypt frame

# Function to open the Encrypt window
def create_encrypt_frame():
    global encrypt_frame, image_label
    encrypt_frame = tk.Frame(root, bg='black')

    # Choose Image Button
    choose_image_button = tk.Button(encrypt_frame, text="Choose Image", command=choose_image, bg='#3d85c6', fg='white', font=('Times New Roman', 14))
    choose_image_button.pack(pady=10)

    # Secret Key Entry for encryption
    secret_key_entry_encrypt = tk.Entry(encrypt_frame, width=30, font=('Times New Roman', 14))
    secret_key_entry_encrypt.pack(pady=10)
    secret_key_entry_encrypt.insert(0, "Enter Secret Key for Encryption")

    # Encrypt Button 
    encrypt_button = tk.Button(encrypt_frame, text="Encrypt", bg='#3d85c6', fg='white', font=('Times New Roman', 14))
    encrypt_button.pack(pady=10)

    # Label to display the selected image path
    image_label = tk.Label(encrypt_frame, text="No image selected", bg='black', fg='white', font=("Arial", 12))
    image_label.pack(pady=5)

    # Large Textbox for encrypted text output
    encrypted_text_box = tk.Text(encrypt_frame, wrap="word", width=40, height=10, font=("Arial", 12))
    encrypted_text_box.pack(pady=10)
    encrypted_text_box.insert("1.0", "Encrypted text will appear here...")  # Optional placeholder text

    # Back Button to switch to the main menu
    back_button_encrypt = tk.Button(encrypt_frame, text="Back", command=show_main_frame, bg='#3d85c6', fg='white', font=('Times New Roman', 14))
    back_button_encrypt.pack(pady=20)

# Function to open the Decrypt window
def create_decrypt_frame():
    global decrypt_frame, decrypted_image_label
    decrypt_frame = tk.Frame(root, bg='black')

    # Large Textbox for encrypted text input
    encrypted_text_input = tk.Text(decrypt_frame, wrap="word", width=40, height=10, font=("Arial", 12))
    encrypted_text_input.pack(pady=10)
    encrypted_text_input.insert("1.0", "Paste encrypted text here...")  # Optional placeholder text

    # Secret Key Entry for decryption
    secret_key_entry_decrypt = tk.Entry(decrypt_frame, width=30, font=('Times New Roman', 14))
    secret_key_entry_decrypt.pack(pady=10)
    secret_key_entry_decrypt.insert(0, "Enter Secret Key for Decryption")

    # Decrypt Button
    decrypt_button = tk.Button(decrypt_frame, text="Decrypt", bg='#3d85c6', fg='white', font=('Times New Roman', 14), command=lambda: display_decrypted_image(decrypt_window))
    decrypt_button.pack(pady=10)

    # Label to show the decrypted image
    decrypted_image_label = tk.Label(decrypt_frame, bg='black')
    decrypted_image_label.pack(pady=10)

    # Back Button to switch to the main menu
    back_button_decrypt = tk.Button(decrypt_frame, text="Back", command=show_main_frame, bg='#3d85c6', fg='white', font=('Times New Roman', 14))
    back_button_decrypt.pack(pady=20)

# Function to display the decrypted image (placeholder for actual decryption logic)
def display_decrypted_image(window):
    # Placeholder image path for demonstration; replace with decrypted image path
    decrypted_image_path = chosen_image_path  # Replace with the path of the actual decrypted image
    
    if decrypted_image_path:
        # Load and resize the image to fit within the label
        image = Image.open(decrypted_image_path)
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        # Update the label with the decrypted image
        decrypted_image_label.config(image=photo)
        decrypted_image_label.image = photo  # Keep a reference to prevent garbage collection
    else:
        decrypted_image_label.config(text="No decrypted image to display")

# Function to show the main frame
def show_main_frame():
    main_frame.pack(fill="both", expand=True)
    encrypt_frame.pack_forget()  # Hide the encrypt frame
    decrypt_frame.pack_forget()  # Hide the decrypt frame

# Create the main application window
root = tk.Tk()
root.title("Image Encryption")
root.geometry("700x400")
root.configure(bg='black')

# Set custom font for the label and buttons
font_style = tkFont.Font(family="Times New Roman", size=20, weight="bold")
button_font_style = tkFont.Font(family="Times New Roman", size=16)

# Create a frame for the main menu
main_frame = tk.Frame(root, bg='black')
main_frame.pack(fill="both", expand=True)

# Create a label for the title
title_label = tk.Label(main_frame, text="IMAGE <=======> TEXT", bg='black', fg='#3d85c6', font=font_style)
title_label.pack(pady=(50, 20))  # Center title label with padding

# Create a frame to hold the buttons
button_frame = tk.Frame(main_frame, bg='black')
button_frame.pack(pady=(10, 0))  # Reduced padding to center the buttons below the title

# Create Encrypt button
encrypt_button = tk.Button(button_frame, text="Encrypt", command=show_encrypt_frame, bg='#3d85c6', fg='white', font=button_font_style, width=15, height=3)
encrypt_button.pack(side=tk.LEFT, padx=(0, 5))  # Small space to the right

# Create Decrypt button
decrypt_button = tk.Button(button_frame, text="Decrypt", command=show_decrypt_frame, bg='#3d85c6', fg='white', font=button_font_style, width=15, height=3)
decrypt_button.pack(side=tk.LEFT, padx=(5, 0))  # Small space to the left

# Initialize chosen image path variable
chosen_image_path = None

# Create the frames for encrypt and decrypt
create_encrypt_frame()
create_decrypt_frame()

# Show the main frame initially
show_main_frame()

# Run the main event loop
root.mainloop()