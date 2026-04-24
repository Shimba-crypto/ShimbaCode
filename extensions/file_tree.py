import os
import customtkinter as ctk

def run(editor):
    files = [f for f in os.listdir(".") if f.endswith((".py", ".lua", ".txt"))]
    for filename in files:
        btn = ctk.CTkButton(editor.sidebar_frame, text=filename, height=20, command=lambda f=filename: editor.open_file(f))
        btn.pack(pady=2, padx=10, fill="x")
