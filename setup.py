#!/usr/bin/python3
import sys, subprocess
import os

dependencies = ['requests', 'beautifulsoup4']

# Install dependencies
if os.name == 'nt':
    subprocess.call([sys.executable, '-m', 'pip', 'install'] + dependencies)
else:
    for n in dependencies:
        os.system('pip install ' + n)
