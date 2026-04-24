import subprocess
import threading

def run(editor):
    # This runs cmd.exe and sends the output to your editor's console
    process = subprocess.Popen(
        ['cmd.exe'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True,
        bufsize=1
    )

    def read_output(pipe):
        for line in iter(pipe.readline, ''):
            editor.show_output(line.strip())

    threading.Thread(target=read_output, args=(process.stdout,), daemon=True).start()
    threading.Thread(target=read_output, args=(process.stderr,), daemon=True).start()

    def send_command(command):
        if process.poll() is None:
            process.stdin.write(command + "\n")
            process.stdin.flush()

    editor.send_to_terminal = send_command
    editor.show_output("Terminal extension linked.")
