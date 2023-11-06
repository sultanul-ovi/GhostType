from os_detect import detect_and_print_operating_system

from credentials_manager import store_credentials


# Part 01 + Part 02
#  run the prerequisite.py


# Part 03:
# -------------
# Use the function from os_detect module
detected_os = detect_and_print_operating_system()
print(f"The operating system detected by the main program is: {detected_os}")



# Store encrypted credentials
credentials = store_credentials()

# Store the encrypted username and password
encrypted_username = credentials['encrypted_username']
encrypted_password = credentials['encrypted_password']

# Use the encrypted credentials as needed
print(f"Encrypted Username: {encrypted_username}")
print(f"Encrypted Password: {encrypted_password}")
