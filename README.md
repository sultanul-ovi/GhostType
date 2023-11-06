<h1 align="center">
   <img src="https://github.com/sultanul-ovi/GhostType/banner.png"  width="200" height="200" />
<br> GhostType: Cross-Platform Keylogger with Stealth Capabilities </br>
</h1>

<h4 align="center">
A sophisticated educational tool for demonstrating keylogging and anti-keylogging techniques.
</h4>



## Project Description
"GhostType" is a cross-platform keylogger designed with stealth capabilities for use in educational and security testing environments. This tool enables users to understand and demonstrate the operation of keyloggers and the effectiveness of security measures against them. By simulating the behavior of malicious keyloggers, "GhostType" serves as a resource for cybersecurity educators, students, and professionals to explore the vulnerabilities and defenses of information systems within an ethical framework.

## Built With

* **Python 3.6.5** - [https://www.python.org/](https://www.python.org/)

## Inputs To Mail.
Get Keyboard,Mouse,ScreenShot,Microphone Inputs and Send to your Mail.
Purpose of the project is testing the security of information systems

## Core Features

1. **Cross-Platform Functionality**:
   - Operable on Windows, macOS, and Linux.
   - Uniform user experience and functionality across all supported operating systems.

2. **Stealth Operation**:
   - Advanced evasion techniques to prevent detection by most antivirus software.
   - Operates discreetly in the background with minimal system footprint.

3. **Email Integration**:
   - Secure email reporting system for sending logged keystrokes at user-defined intervals.
   - Encrypted email content to ensure the confidentiality of logged information.

4. **User Consent Protocol**:
   - Built-in features to ensure the tool is used only with informed consent from all parties involved.
   - Automated consent verification before logging begins.

5. **Customizable Logging**:
   - Options to specify what types of input to log (keystrokes, mouse clicks, etc.).
   - Ability to filter and log only specific applications or inputs based on user settings.

6. **Self-Destruction Mechanism**:
   - Ability to self-delete if certain user-defined conditions are met, such as unauthorized access attempts.

7. **RSA Encryption**:
   - Real-time RSA encryption of logs to protect against unauthorized access to data.
   - Private key held only by the user, ensuring that intercepted logs cannot be decrypted.

8. **User Education and Documentation**:
   - Comprehensive documentation on how to use and customize "GhostType".
   - Educational materials outlining keylogging mechanisms, legal considerations, and how to safeguard against malicious use.

9. **Modular Architecture**:
   - Ease of extending and adding new features or integrations.
   - Plugin system to incorporate additional functionality like screen capture or microphone logging.

10. **Contribution to Cybersecurity**:
    - Guidelines for contributing findings to the cybersecurity community.
    - Promotion of ethical hacking practices and responsible disclosure.

11. **Open Source Development**:
    - Source code available for review, modification, and contribution.
    - Community-driven enhancements and support.

12. **Legal and Ethical Disclaimer**:
    - Strong emphasis on legal compliance and ethical usage with a clear disclaimer and usage policy.
    - Commitment to transparency and ethical conduct in all project aspects.


# Project Code Summaries

Here are the functionalities provided by each script in my project, each serving a distinct purpose in the application's ecosystem.

## install_packages.py

- The `install_packages_from_requirements` function in this script handles Python package installation. It employs the `subprocess` module to automate the setup of required packages listed in a `requirements.txt` file.

## update_packages.py

- With functions to retrieve and update installed packages, this script ensures that the Python environment remains current, utilizing `pip` to upgrade packages to their latest versions.

## prerequisite.py

- This initialization script uses `install_packages_from_requirements` to install necessary dependencies and calls `update_packages` to keep them updated. It's a key part of setting up the environment before running the main application.

## os_detect.py

- This script provides the `detect_and_print_operating_system` function, which uses the `platform` module to identify and return the current operating system. It covers detection for macOS, Windows, Linux, and defaults to 'unknown' for other OS types.

## credentials_manager.py

- This script manages secure credential storage by providing a user interface for credential input and using AES encryption for real-time encryption. It ensures the secure handling of sensitive information within the application.

## main.py

- Acting as the orchestrator, this file uses functions from `os_detect` and `credentials_manager` to detect the OS and manage encrypted credentials. It references `prerequisite.py` for initial setup, indicating its role in preparing the application for execution.

## keylogger.py

- This script contains the `KeyLogger` class that captures keyboard input, takes screenshots, and records audio. It imports essential modules and installs any that are missing. Once initialized with email credentials, it can dispatch the logged data via email.




---

# Keylogger Program Summary

This program is a robust keylogger with additional surveillance capabilities. Here's an overview of its core components and their functions:

1. **Imports and Error Handling**:
   - This component imports the necessary modules for logging, screenshots, audio recording, and email sending. If a module is missing, it automatically installs it using `pip3`.

2. **Email Credentials and Report Interval**:
   - This function uses placeholders for email credentials (`EMAIL_ADDRESS` and `EMAIL_PASSWORD`) to send captured data. The report interval (`SEND_REPORT_EVERY`) determines how often these reports are dispatched.

3. **KeyLogger Class**:
   - The `KeyLogger` class, when initialized, sets up email delivery with a specific time interval. This class has methods for logging various activities, sending email reports, and collecting system information.

4. **Reporting and Execution**:
   - The `report` method manages the periodic sending of captured logs. The `run` method establishes listeners for capturing data and ensures continuous operation of the script.

5. **Self-Termination**:
   - This functionality is designed for the script to self-delete after its operation to evade detection, with specific routines for Windows and Unix-like systems.

6. **Instantiation and Running**:
   - An instance of the `KeyLogger` class is created with defined intervals and credentials, and its `run` method is invoked to start the monitoring process.

Each component of this keylogger is meticulously crafted to ensure comprehensive monitoring and stealthy operation, showcasing advanced scripting and automation capabilities.













## INSTALLATION

**You don't need to do anything for installation just run the script**

![github-small](/images/Adsız.png)

## USAGE

•**Create an account on "https://mailtrap.io/" using a temp mail.**

•**Set your own SMTP USERNAME and SMTP PASSWORD on "keylogger.py".**

•**pip install -r requirements.txt**

•**python3 keylogger.py**

•**Every 10 seconds,You Get the Data from the Target Computer**

•**If Target finds the Code and Open the File for Want to Learn your MAIL and Password The Program DELETE itself.**


## ANTIVIRUS TEST

![github-small](/images/1.png)

![github-small](/images/2.png)

#### Acknowledgments

> I'd like to express my gratitude for the inspiration I've drawn from the works of [Hussein Bakri](https://github.com/HusseinBakri), [Casey Scarborough](https://github.com/caseyscarborough), and [Giacomo Lawrance](https://github.com/GiacomoLaw) on GitHub. Their innovative and insightful projects have been invaluable in guiding the design and development of my own work. Their commitment to sharing knowledge and fostering open-source collaboration has profoundly impacted my approach to this project, and for that, I am deeply appreciative.

#### Disclaimer

> This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this tool and software in general.

---
