import subprocess

def run(editor_instance):
    file_path = editor_instance.get_current_file_path()
    
    if not file_path:
        print("Error: No file open to run.")
        return

    try:
        # Run the python file and capture output
        result = subprocess.run(
            ['python', file_path], 
            capture_output=True, 
            text=True, 
            check=True
        )
        editor_instance.show_output(result.stdout)
    except subprocess.CalledProcessError as e:
        editor_instance.show_output(f"Error:\n{e.stderr}")
