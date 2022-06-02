import subprocess
import sys


__install_list__ = 'requirements.txt'

if __name__ == '__main__':
    py = sys.executable
    subprocess.call([py, '-m', 'ensurepip', '--default-pip'])
    subprocess.call([py, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.call([py, '-m', 'pip', 'install', 'numpy'])
    subprocess.call([py, '-m', 'pip', 'install', '-r', __install_list__])
    subprocess.call([py, '-m', 'pip', 'install', 'opencv-contrib-python-headless~=4.5.1'])
