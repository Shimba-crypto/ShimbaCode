def run(editor_instance):
    # This is your extension logic
    # You can pass 'editor_instance' to allow the extension to control the UI
    print("ShimbaCode Extension Loaded!")
    editor_instance.insert_text("Hello from the extension!")
