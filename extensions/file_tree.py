import os
import customtkinter as ctk

def run(editor):
    # Get all files in the current directory
    files = [f for f in os.listdir(".") if f.endswith((".py", ".lua", ".txt"))]
    
    # Create buttons for each file
    for filename in files:
        btn = ctk.CTkButton(
            editor.extensions_frame, 
            text=filename, 
            height=20, 
            command=lambda f=filename: editor.open_file(f)
        )
        btn.pack(pady=2, padx=10, fill="x")
