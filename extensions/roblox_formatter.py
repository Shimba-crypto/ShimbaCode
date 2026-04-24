def run(editor):
    content = editor.get_text()
    
    # 1. Add branding if missing
    if "-- itsShimbaYT" not in content:
        content = "-- itsShimbaYT\n" + content
    
    # 2. Basic cleanup
    formatted = content.replace("\t", "    ")
    
    # 3. Apply
    editor.set_text(formatted)
    editor.show_output("Code formatted: Branding applied.")
