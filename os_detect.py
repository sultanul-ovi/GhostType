
import platform

def detect_and_print_operating_system():
    """
    Detects the operating system being used, prints it, and returns a string indicating it.
    Possible return values are 'Windows', 'macOS', 'Linux', or 'unknown'.
    """
    os_name = platform.system()
    if os_name == 'Darwin':
        detected_os = 'macOS'
    elif os_name == 'Windows':
        detected_os = 'Windows'
    elif os_name == 'Linux':
        detected_os = 'Linux'
    else:
        detected_os = 'unknown'
    
    # # Print the operating system
    # print(f"Detected operating system: {detected_os}")
    
    
    return detected_os
