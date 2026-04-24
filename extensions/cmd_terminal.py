import subprocess
import threading
import os

def run(editor_instance):
    # Setup the subprocess for cmd.exe
    # We use pipes to communicate with the process in the background
    process = subprocess.Popen(
        ['cmd.exe'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True,
        bufsize=1
    )

    def read_output():
        while True:
            line = process.stdout.readline()
            if not line:
                break
            editor_instance.show_output(line.strip())
            
    def read_errors():
        while True:
            line = process.stderr.readline()
            if not line:
                break
            editor_instance.show_output(f"ERR: {line.strip()}")

    # Start threads to read stdout and stderr so the GUI doesn't freeze
    threading.Thread(target=read_output, daemon=True).start()
    threading.Thread(target=read_errors, daemon=True).start()

    # Create a command input method for the editor
    def send_command(command):
        if process.poll() is None: # Check if process is still running
            process.stdin.write(command + "\n")
            process.stdin.flush()

    # Attach the send_command method to the editor instance
    editor_instance.send_to_terminal = send_command
    editor_instance.show_output("Terminal Ready: cmd.exe linked.")
