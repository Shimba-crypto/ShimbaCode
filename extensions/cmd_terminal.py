import subprocess
import threading

def run(editor):
    process = subprocess.Popen(['cmd.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, bufsize=1)
    
    def read_pipe(pipe):
        for line in iter(pipe.readline, ''):
            editor.show_output(line.strip())
            
    threading.Thread(target=read_pipe, args=(process.stdout,), daemon=True).start()
