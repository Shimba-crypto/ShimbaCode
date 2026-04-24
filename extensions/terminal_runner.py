import subprocess
import os

def run(editor_instance):
    # 1. Get the current code from the editor
    code = editor_instance.get_text()
    file_path = editor_instance.get_current_file_path()

    # 2. If no file is open, save to a temp file so we can run it anyway
    if not file_path:
        file_path = "temp_run.py"
    
    # 3. Auto-save current content to the file before running
    try:
        with open(file_path, "w") as f:
            f.write(code)
    except Exception as e:
        editor_instance.show_output(f"Error saving file: {e}")
        return

    # 4. Run the python file and capture output safely
    try:
        editor_instance.show_output(f"--- Running {file_path} ---")
        
        # Use subprocess.run to execute the file
        result = subprocess.run(
            ['python', file_path], 
            capture_output=True, 
            text=True, 
            check=False # We handle errors manually below
        )
        
        # Display Standard Output
        if result.stdout:
            editor_instance.show_output(result.stdout)
            
        # Display Errors if they occur
        if result.stderr:
            editor_instance.show_output(f"Python Error:\n{result.stderr}")
            
    except Exception as e:
        editor_instance.show_output(f"System Error: {str(e)}")
