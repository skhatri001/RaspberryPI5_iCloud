import subprocess
import numpy as np
import os
import shlex
os.chdir('/home/skhatri007/Dropbox-Uploader')
# os.getcwd()
#subprocess.call(shlex.split('./test.sh param1 param2'))

output = subprocess.run(shlex.split('./dropbox_uploader.sh list /'))
print(output)
