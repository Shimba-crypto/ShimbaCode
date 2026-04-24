import customtkinter as ctk
import urllib.request
import json
import threading

def run(editor):
    # --- Sidebar UI ---
    label = ctk.CTkLabel(editor.sidebar_frame, text="DISCORD NOTIFIER", font=("Arial", 12, "bold"))
    label.pack(pady=(20, 5))

    url_entry = ctk.CTkEntry(editor.sidebar_frame, placeholder_text="Webhook URL")
    url_entry.pack(fill="x", padx=10, pady=5)

    msg_entry = ctk.CTkEntry(editor.sidebar_frame, placeholder_text="Message")
    msg_entry.pack(fill="x", padx=10, pady=5)

    # --- Logic ---
    def send_webhook():
        url = url_entry.get()
        msg = msg_entry.get()
        
        if not url or not msg:
            editor.show_output("Error: URL and Message required.")
            return

        def task():
            try:
                data = json.dumps({"content": msg}).encode('utf-8')
                req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
                urllib.request.urlopen(req)
                editor.show_output("Discord: Message sent successfully!")
            except Exception as e:
                editor.show_output(f"Discord Error: {e}")

        # Run in thread so the UI doesn't freeze while sending
        threading.Thread(target=task, daemon=True).start()

    send_btn = ctk.CTkButton(editor.sidebar_frame, text="Send to Discord", command=send_webhook, fg_color="#7289da")
    send_btn.pack(fill="x", padx=10, pady=5)
