import os
import customtkinter as ctk

def run(editor):
    sidebar = editor.sidebar_frame
    
    # Label for the file tree
    tree_label = ctk.CTkLabel(sidebar, text="FILES", font=("Arial", 12, "bold"))
    tree_label.pack(pady=(10, 5))
    
    # List files
    for filename in os.listdir("."):
        if filename.endswith((".py", ".lua", ".txt")):
            btn = ctk.CTkButton(
                sidebar, 
                text=filename, 
                height=20,
                command=lambda f=filename: editor.open_file(f)
            )
            btn.pack(pady=2, padx=10, fill="x")
