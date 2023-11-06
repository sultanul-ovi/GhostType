
import subprocess
import sys

# Function to install packages from a requirements.txt file
def install_packages_from_requirements(requirements_file_path):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file_path])

