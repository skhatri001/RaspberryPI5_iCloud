import subprocess
import numpy as np
import os
os.chdir('/home/skhatri007/Dropbox-Uploader')
# os.getcwd()
output = subprocess.call(['./dropbox_uploader.sh','list /'])
print(output)