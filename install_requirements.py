
import os
import subprocess

def install_dependencies():
    # Check if pip is installed
    try:
        subprocess.check_call(['pip', '--version'])
    except FileNotFoundError:
        print("pip is not installed. Run 'python get_pip.py' to install it.")
        return
    
    # Install dependencies from requirements.txt
    subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

if __name__ == "__main__":
    install_dependencies()
