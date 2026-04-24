import os
import platform

def run(editor):
    def show_stats():
        info = f"--- SYSTEM INFO ---\nOS: {platform.system()}\nPython: {platform.python_version()}\nRoot: {os.getcwd()}\n------------------"
        editor.show_output(info)
        
    import customtkinter as ctk
    btn = ctk.CTkButton(editor.sidebar_frame, text="Sys Stats", command=show_stats, fg_color="#f1c40f", text_color="black")
    btn.pack(pady=5, padx=10, fill="x")
