import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import base64
import os


class FileEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryptor/Decryptor")
        self.root.geometry("400x400")  # Dimensioni finestra
        self.root.resizable(False, False)  # Disabilita ridimensionamento

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(expand=True)

        self.title_label = tk.Label(self.frame, text="File Encryptor/Decryptor", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.load_button = tk.Button(self.frame, text="Carica File", command=self.load_file, width=20, height=2,
                                     bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.load_button.pack(pady=10)

        self.password_label = tk.Label(self.frame, text="Inserisci Password:", font=("Helvetica", 12))
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(self.frame, show="*", width=30, font=("Helvetica", 12))
        self.password_entry.pack(pady=5)

        self.encrypt_button = tk.Button(self.frame, text="Cripta File", command=self.encrypt_file, width=20, height=2,
                                        bg="#2196F3", fg="white", font=("Helvetica", 12))
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(self.frame, text="Decripta File", command=self.decrypt_file, width=20, height=2,
                                        bg="#FF5722", fg="white", font=("Helvetica", 12))
        self.decrypt_button.pack(pady=10)

        self.filepath = None

    def load_file(self):
        self.filepath = filedialog.askopenfilename()
        if self.filepath:
            messagebox.showinfo("File Selezionato", f"File caricato: {self.filepath}")

    def encrypt_file(self):
        if not self.filepath:
            messagebox.showwarning("Nessun File", "Per favore, carica un file prima di criptare.")
            return

        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Nessuna Password", "Per favore, inserisci una password.")
            return

        key = base64.urlsafe_b64encode(password.encode('utf-8').ljust(32)[:32])
        fernet = Fernet(key)

        with open(self.filepath, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        encrypted_filepath = self.filepath + ".encrypted"
        with open(encrypted_filepath, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        messagebox.showinfo("File Criptato", f"File criptato e salvato come: {encrypted_filepath}")

    def decrypt_file(self):
        if not self.filepath:
            messagebox.showwarning("Nessun File", "Per favore, carica un file prima di decriptare.")
            return

        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Nessuna Password", "Per favore, inserisci una password.")
            return

        key = base64.urlsafe_b64encode(password.encode('utf-8').ljust(32)[:32])
        fernet = Fernet(key)

        with open(self.filepath, 'rb') as file:
            encrypted = file.read()

        try:
            decrypted = fernet.decrypt(encrypted)
        except Exception as e:
            messagebox.showerror("Errore", "Decriptazione fallita. Password errata o file corrotto.")
            return

        decrypted_filepath = self.filepath.replace(".encrypted", ".decrypted")
        with open(decrypted_filepath, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        messagebox.showinfo("File Decriptato", f"File decriptato e salvato come: {decrypted_filepath}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileEncryptorApp(root)
    root.mainloop()
