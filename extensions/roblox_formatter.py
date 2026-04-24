def run(editor_instance):
    content = editor_instance.get_text()
    
    # 1. Add your branding watermark if it's not already there
    if "-- itsShimbaYT" not in content:
        content = "-- itsShimbaYT\n" + content
    
    # 2. Simple formatting: Replace tabs with 4 spaces for Luau compatibility
    formatted_content = content.replace("\t", "    ")
    
    # 3. Apply changes back to the editor
    editor_instance.set_text(formatted_content)
    print("Code formatted successfully!")
