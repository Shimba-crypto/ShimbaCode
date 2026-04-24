from tkinter import messagebox
import customtkinter as ctk

def run(editor):
    def trigger_glitch():
        editor.show_output("CRITICAL: Zaza Glitch Detected!")
        messagebox.showwarning("Zaza Defender", "System integrity compromise detected!\nInitiating security scan...")
        editor.show_output("Scan complete. System restored.")

    btn = ctk.CTkButton(editor.sidebar_frame, text="Zaza Glitch", command=trigger_glitch, fg_color="#9b59b6")
    btn.pack(pady=5, padx=10, fill="x")
