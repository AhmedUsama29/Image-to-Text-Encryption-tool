import tkinter as tk

def show_encrypt_page():
    main_frame.pack_forget()
    encrypt_frame.pack(fill="both", expand=True)

def show_decrypt_page():
    main_frame.pack_forget()
    decrypt_frame.pack(fill="both", expand=True)

def show_main_page():
    encrypt_frame.pack_forget()
    decrypt_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

# Initialize the root window
root = tk.Tk()
root.title("IMAGE <=> TEXT")
root.geometry("800x500")
root.configure(bg='black')

# Main Frame
main_frame = tk.Frame(root, bg='black')
title_label = tk.Label(main_frame, text="IMAGE <=> TEXT", font=("Arial", 24), fg="white", bg="black")
title_label.pack(pady=20)

# Encrypt and Decrypt Buttons on Main Page
encrypt_button = tk.Button(main_frame, text="Encrypt", font=("Arial", 14), bg="#3d85c6", fg="white", command=show_encrypt_page)
decrypt_button = tk.Button(main_frame, text="Decrypt", font=("Arial", 14), bg="#3d85c6", fg="white", command=show_decrypt_page)
encrypt_button.pack(pady=10)
decrypt_button.pack(pady=10)

# Encrypt Frame
encrypt_frame = tk.Frame(root, bg='black')
encrypt_title = tk.Label(encrypt_frame, text="Encrypt", font=("Arial", 18), fg="white", bg="black")
encrypt_title.pack(pady=10)

# Choose Image Button (Example component)
choose_image_button = tk.Button(encrypt_frame, text="Choose Image", bg='#3d85c6', fg='white', font=('Times New Roman', 14))
choose_image_button.pack(pady=10)

# Secret Key Entry for encryption
secret_key_entry_encrypt = tk.Entry(encrypt_frame, width=30, font=('Times New Roman', 14))
secret_key_entry_encrypt.pack(pady=10)
secret_key_entry_encrypt.insert(0, "Enter Secret Key for Encryption")

# Encrypt Button
encrypt_button_frame = tk.Button(encrypt_frame, text="Encrypt", bg='#3d85c6', fg='white', font=('Times New Roman', 14))
encrypt_button_frame.pack(pady=10)


# Textbox for input text to encrypt
text_input_encrypt = tk.Text(encrypt_frame, wrap="word", width=40, height=10, font=("Arial", 12))
text_input_encrypt.pack(pady=10)
text_input_encrypt.insert("1.0", "Enter text to encrypt...")  # Optional placeholder text

# Back Button on Encrypt Page
back_button_encrypt = tk.Button(encrypt_frame, text="Back", command=show_main_page, bg='#3d85c6', fg='white', font=('Times New Roman', 20))
back_button_encrypt.place(x=10, rely=1.0, anchor="sw")  

# Decrypt Frame
decrypt_frame = tk.Frame(root, bg='black')
decrypt_title = tk.Label(decrypt_frame, text="Decrypt", font=("Arial", 18), fg="white", bg="black")
decrypt_title.pack(pady=10)

# Textbox for encrypted text input
encrypted_text_input = tk.Text(decrypt_frame, wrap="word", width=40, height=10, font=("Arial", 12))
encrypted_text_input.pack(pady=10)
encrypted_text_input.insert("1.0", "Paste encrypted text here...")  # Optional placeholder text

# Secret Key Entry for decryption
secret_key_entry_decrypt = tk.Entry(decrypt_frame, width=30, font=('Times New Roman', 14))
secret_key_entry_decrypt.pack(pady=10)
secret_key_entry_decrypt.insert(0, "Enter Secret Key for Decryption")

# Decrypt Button
decrypt_button_frame = tk.Button(decrypt_frame, text="Decrypt", bg='#3d85c6', fg='white', font=('Times New Roman', 14))
decrypt_button_frame.pack(pady=10)

# Back Button on Decrypt Page (Positioned at the bottom left)
back_button_decrypt = tk.Button(decrypt_frame, text="Back", command=show_main_page, bg='#3d85c6', fg='white', font=('Times New Roman', 20))
back_button_decrypt.place(x=10, rely=1.0, anchor="sw")  # Adjust 'y' to fine-tune the bottom spacing

# Show the main page initially
main_frame.pack(fill="both", expand=True)

# Start the main loop
root.mainloop()