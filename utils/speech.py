import pyttsx3
import threading

def speak_text(text):
    """
    Speaks the given text using the pyttsx3 engine.
    Runs in a background thread to prevent the webcam stream and UI from freezing.
    """
    # Fix pronunciation of specific single letters that pyttsx3 struggles with
    pronunciation_map = {
        'Z': 'Zee',
        'z': 'zee',
        'A': 'Ay',
        'a': 'ay'
    }
    
    speak_str = text
    # If the text is exactly a single letter and in our map, substitute it
    if len(text.strip()) == 1 and text.strip() in pronunciation_map:
        speak_str = pronunciation_map[text.strip()]

    def run_speech():
        try:
            # On Windows, COM initialization is required for background threads
            import pythoncom
            pythoncom.CoInitialize()
        except ImportError:
            pass # Ignore if not on Windows or if pythoncom is missing
            
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150) # Set speaking rate
            engine.say(speak_str)
            engine.runAndWait()
        except Exception as e:
            print(f"Text-to-Speech Error: {e}")

    # Start the thread
    thread = threading.Thread(target=run_speech)
    thread.daemon = True
    thread.start()
