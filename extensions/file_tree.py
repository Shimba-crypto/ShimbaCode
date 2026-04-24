import os
import customtkinter as ctk # Assuming you use CustomTkinter

def run(editor_instance):
    # This assumes editor_instance has a 'sidebar_frame' attribute
    sidebar = editor_instance.sidebar_frame
    
    # Clear old items
    for widget in sidebar.winfo_children():
        widget.destroy()
        
    # List all files in the current directory
    for filename in os.listdir("."):
        # Filter for code files
        if filename.endswith((".py", ".lua", ".json")):
            btn = ctk.CTkButton(
                sidebar, 
                text=filename, 
                command=lambda f=filename: editor_instance.open_file(f)
            )
            btn.pack(pady=2, padx=5, fill="x")
