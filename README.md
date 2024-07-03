This code defines a simple graphical user interface (GUI) application for encrypting and decrypting files using the `tkinter` library for the GUI and the `cryptography` library's `Fernet` module for encryption and decryption. Here is a breakdown of the main components and functionality:

### Components:

1. **Imports**:
   - `tkinter`: A standard Python library for creating graphical user interfaces.
   - `filedialog` and `messagebox`: Modules from `tkinter` for file selection dialogs and message boxes.
   - `Fernet` from `cryptography.fernet`: A module for symmetric encryption and decryption.
   - `base64`: For encoding and decoding data to and from Base64.
   - `os`: For interacting with the operating system.

2. **FileEncryptorApp Class**:
   - **Initialization (`__init__` method)**: Sets up the GUI with a title, size, and layout. It includes buttons, labels, and an entry for password input.
     - `self.root`: Main window.
     - `self.frame`: Container for the widgets.
     - `self.title_label`: Label displaying the title.
     - `self.load_button`: Button to load a file.
     - `self.password_label`: Label prompting the user to enter a password.
     - `self.password_entry`: Entry field for the password.
     - `self.encrypt_button`: Button to encrypt the file.
     - `self.decrypt_button`: Button to decrypt the file.
     - `self.filepath`: Variable to store the path of the selected file.

3. **Methods**:
   - **`load_file`**: Opens a file dialog to select a file and displays a message with the selected file path.
   - **`encrypt_file`**: Encrypts the loaded file using the provided password.
     - Checks if a file is loaded and if a password is provided.
     - Generates an encryption key from the password.
     - Reads the file content, encrypts it, and saves it with a ".encrypted" extension.
   - **`decrypt_file`**: Decrypts the loaded file using the provided password.
     - Checks if a file is loaded and if a password is provided.
     - Generates a decryption key from the password.
     - Reads the encrypted file content, decrypts it, and saves it with a ".decrypted" extension.

4. **Main Program Execution**:
   - Creates the main application window and starts the `tkinter` event loop.

### Explanation of Key Steps:

- **Key Generation**: The password is used to generate a 32-byte key suitable for `Fernet`. This is done by encoding the password to bytes, padding/truncating it to 32 bytes, and then encoding it in Base64.
  
- **File Encryption**:
  - Reads the contents of the selected file.
  - Encrypts the contents using the `Fernet` key.
  - Writes the encrypted data to a new file with a ".encrypted" extension.

- **File Decryption**:
  - Reads the contents of the selected encrypted file.
  - Attempts to decrypt the contents using the `Fernet` key.
  - Writes the decrypted data to a new file with a ".decrypted" extension.
  - If decryption fails (e.g., due to an incorrect password or corrupted file), an error message is shown.

### User Interaction:

- The user interacts with the application through a series of buttons and text entries:
  - **"Carica File"**: Opens a file dialog to select a file for encryption or decryption.
  - **Password Entry**: Allows the user to input the password used for encryption/decryption.
  - **"Cripta File"**: Encrypts the selected file using the entered password.
  - **"Decripta File"**: Decrypts the selected file using the entered password.

This application provides a user-friendly interface for basic file encryption and decryption tasks, ensuring that the user can securely encrypt and decrypt files with a password.
