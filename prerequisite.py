from install_packages import install_packages_from_requirements

from update_packages import get_installed_packages, update_packages

# Part 01:
# ------------- 
# Path to the requirements.txt file
requirements_path = 'requirements.txt'  # Update this to the path of your requirements.txt file

# Install the packages
install_packages_from_requirements(requirements_path)


# Part 02:
# -------------
# Update installed packages
installed_packages = get_installed_packages()
update_packages(installed_packages)
print("All packages have been updated.")