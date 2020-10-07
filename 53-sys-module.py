#sys is to interact closely with the interpreter
#it's allways present
import sys
from os.path import dirname, abspath

#adding a new path
sys.path.append("users/documents")

#this goes to the parent directory
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import utils #it's going to work
#even if utils.py is in a subfolder

print(sys.path)