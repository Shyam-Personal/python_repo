# Que : Import file from f1 folfer in f2 folder
import sys, os
print(os.getcwd())
sys.path.append(os.getcwd())
print(sys.path)
# from folder.filname import function
from f1.f1 import f1

print("in f2")
f1()