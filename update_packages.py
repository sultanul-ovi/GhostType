
import pkg_resources
import subprocess
import sys

# Function to get the list of installed packages
def get_installed_packages():
    installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]
    return installed_packages

# Function to update packages using pip
def update_packages(packages):
    for package, version in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', package])

