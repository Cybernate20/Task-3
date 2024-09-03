import tkinter as tk
from tkinter import messagebox


def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message


def process_text():
    message = entry_message.get()

    
    if not message:
        messagebox.showerror("Error", "Please enter a message.")
        return
    
    
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer!")
        return

    
    choice = var.get()

    if choice == 1:  # Encrypt
        result = encrypt(message, shift)
    elif choice == 2:  # Decrypt
        result = decrypt(message, shift)
    else:
        messagebox.showerror("Error", "Please select Encrypt or Decrypt.")
        return

    
    label_result.config(text="Result: " + result)


window = tk.Tk()
window.title("Nathan's Caesar Cipher")
window.geometry("400x300")
window.configure(bg="brown")  


label_message = tk.Label(window, text="Enter your message:", bg="brown", fg="black", font=("Arial", 12))
label_message.pack(pady=10)
entry_message = tk.Entry(window, width=30, font=("Arial", 12))
entry_message.pack(pady=5)


label_shift = tk.Label(window, text="Enter the shift value:", bg="brown", fg="black", font=("Arial", 12))
label_shift.pack(pady=10)
entry_shift = tk.Entry(window, width=10, font=("Arial", 12))
entry_shift.pack(pady=5)


var = tk.IntVar()
radio_encrypt = tk.Radiobutton(window, text="Encrypt", variable=var, value=1, bg="brown", fg="black", font=("Arial", 12))
radio_encrypt.pack(pady=5)
radio_decrypt = tk.Radiobutton(window, text="Decrypt", variable=var, value=2, bg="brown", fg="black", font=("Arial", 12))
radio_decrypt.pack(pady=5)


button_process = tk.Button(window, text="Process", command=process_text, bg="white", font=("Arial", 12))
button_process.pack(pady=20)


label_result = tk.Label(window, text="Result: ", bg="brown", fg="black", font=("Arial", 12))
label_result.pack(pady=10)


window.mainloop()